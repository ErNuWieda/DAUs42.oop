"""
Hauptmodul der DAUs42-Anwendung.
Definiert die Klasse DAUApp, die das Hauptfenster, die Benutzeroberfläche und die Kernlogik der Anwendung verwaltet.
"""
import tkinter as tk
from tkinter import messagebox, ttk, Menu
from PIL import Image, ImageTk
import os
import pathlib
import random
import platform
import threading # Für fake_optimization

from . import constants
from .sound import DAUSound
from .actions import ActionHandler # Geänderter Import
from .ui_helpers import add_tooltip
from .system_info import get_platform_display_text, get_os_details
# from .dialogs import create_sarcastic_countdown_dialog, create_show_progress_dialog, run_fake_optimization_steps_dialog, create_sidefx_dialog, create_warning_dialog
from .dialogs import DialogFactory # Geänderter Import

class DAUApp:
    """
    Die Hauptanwendungsklasse für "DAUs forty-two - Das Sinnfrei-Tool".

    Diese Klasse ist verantwortlich für:
    - Initialisierung des Hauptfensters (root Tkinter Instanz).
    - Einrichten der Menüleiste, des Hintergrundbildes und der UI-Komponenten (Buttons, Labels).
    - Binden von Events (z.B. Tastenkombinationen).
    - Handhabung von Aktionen, die durch Benutzerinteraktionen ausgelöst werden."""
    def __init__(self, root_tk_instance):
        """Initialisiert die Hauptanwendung."""
        self.root = root_tk_instance
        self.root.title("DAUs forty-two - Das Sinnfrei-Tool")
        self.root.geometry("500x550") # Etwas mehr Platz für das Plattform-Label
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", self._handle_exit_exception)
        self.bg = self._load_bg(bg_name="hitchhikers.jpg")
      
        # Instanzen der Handler/Factory-Klassen erstellen
        self.action_handler = ActionHandler()
        self.dialog_factory = DialogFactory()

        # Mache das Hauptfenster sichtbar, falls es via root.withdraw() versteckt war
        self.root.deiconify()
        self._setup_menubar()
        self._setup_background_image()
        self._setup_ui_components()
        self._bind_events()
                
    def _load_bg(self, bg_name):
        """
        Lädt ein Hintergrundbild und passt dessen Größe an die Fenstergröße an.

        Args:
            bg_name (str): Der Dateiname des Hintergrundbildes im 'assets'-Ordner.

        Returns:
            ImageTk.PhotoImage: Das für Tkinter vorbereitete Bildobjekt.
        """
        ASSETS_BASE_DIR = pathlib.Path(__file__).resolve().parent.parent / "assets"
        filepath = ASSETS_BASE_DIR / bg_name
        bild = Image.open(filepath)
        bild = bild.resize((500, 550))
        bild_tk = ImageTk.PhotoImage(bild)
        return bild_tk

    def _handle_exit_exception(self, event=None):
        """
        Behandelt den Versuch, das Fenster über den Schließen-Button (WM_DELETE_WINDOW) zu schließen.
        Zeigt stattdessen eine humorvolle Fehlermeldung an.
        """
        messagebox.showerror("Erwarteter Bedienerfehler", 
                             "DAU exception, line 42,\ne: deprecated value 'WM_DELETE_WINDOW' not accepted!", 
                             parent=self.root)
        
    def _setup_menubar(self):
        """Erstellt und konfiguriert die Menüleiste der Anwendung."""
        menubar = Menu(self.root)

        # Datei-Menü
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Neue Sinnlosigkeit", command=lambda: self.action_handler.menu_show_sinnlosigkeit(self.root))
        file_menu.add_command(label="Alles rückgängig machen", command=lambda: self.action_handler.menu_show_undo_too_late(self.root))
        file_menu.add_separator()
        file_menu.add_command(label="Beenden?", command=self._handle_sarcastic_exit_prompt)
        menubar.add_cascade(label="Datei", menu=file_menu)

        # Extras-Menü
        extra_menu = Menu(menubar, tearoff=0)
        extra_menu.add_command(label="Unsichtbare Optionen anzeigen", command=lambda: self.action_handler.menu_show_invisible_options_error(self.root))
        extra_menu.add_command(label="Nichts tun", command=lambda: self.action_handler.menu_do_nothing_warning(self.root))
        extra_menu.add_command(label="System analysieren", command=self._action_show_progress)
        extra_menu.add_command(label="System optimieren", command=self._action_fake_optimization)
        menubar.add_cascade(label="Extras", menu=extra_menu)

        # Hilfe-Menü
        help_menu = Menu(menubar, tearoff=0)
        help_menu.add_command(label="Was soll das alles?", command=lambda: self.action_handler.menu_show_help_purpose(self.root))
        help_menu.add_command(label="Easter Egg finden", command=lambda: self.action_handler.menu_show_easter_egg(self.root)) # Auch per Ctrl+B
        menubar.add_cascade(label="Hilfe", menu=help_menu)

        # Meta-Menü
        meta_menu = Menu(menubar, tearoff=0)
        meta_menu.add_command(label="Beipackzettel", command=self._call_sidefx_dialog)
        meta_menu.add_command(label="⚠ Wichtig! ⚠", command=self._call_warning_dialog)
        meta_menu.add_separator()
        meta_menu.add_command(label="Über DAUs forty-two", command=lambda: self.action_handler.menu_show_about(self.root))
        menubar.add_cascade(label="Meta", menu=meta_menu)

        self.root.config(menu=menubar)

    def _setup_background_image(self):
        """Platziert das Hintergrundbild im Hauptfenster."""
        self.bg_image = self.bg
        # Label mit Bild, füllt das ganze Fenster
        self.bg_label = tk.Label(self.root, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    def _setup_ui_components(self):
        """Erstellt und platziert die primären UI-Komponenten (Labels, Buttons) im Hauptfenster."""
        tk.Label(self.root, text="Willkommen bei DAUs forty-two", font=("Helvetica", 16)).pack(pady=10)
        tk.Label(self.root, text="(DAU-Mode für Dummies aktiv)", font=("Helvetica", 11), fg="green").pack(pady=5) # pady reduziert
        
        platform_label_text = get_platform_display_text()
        platform_label = tk.Label(self.root, text=platform_label_text, font=("Helvetica", 9), fg="gray")
        platform_label.pack(pady=5)

        # Konfiguration für die Standard-Aktionsbuttons
        buttons_config = [
            ("Internet drucken", lambda: self.action_handler.print_internet(self.root), "Druckt das gesamte Internet auf Recyclingpapier"),
            ("DAU-Konsole öffnen", lambda: self.action_handler.dau_console(self.root), "Für Menschen mit fragwürdigem IT-Wissen"),
            ("Ultimative Antwort generieren", lambda: self.action_handler.ultimate_answer(self.root), "Antwort auf das Leben, das Universum und den ganzen Rest"),
            ("Zufällige Ausrede", lambda: self.action_handler.random_excuse(self.root), "Wenn du wieder Mist gebaut hast – blame the Hamster"),
        ]

        for text, command, tooltip in buttons_config:
            btn = tk.Button(self.root, text=text, command=command)
            btn.pack(pady=5, fill=tk.X, padx=50) # fill und padx für bessere Optik
            add_tooltip(btn, tooltip)
            
        # Spezielle Buttons
        btn_panic = tk.Button(self.root, text="Don't Panic!", command=self._action_dont_panic, bg="gold", fg="darkred")
        btn_panic.pack(pady=5, fill=tk.X, padx=50)
        add_tooltip(btn_panic, "Beruhigung für angehende IT-Apokalypsen")

        btn_expert = tk.Button(self.root, text="GOD-Mode für Mutige", command=self._action_confirm_expert_mode, fg="blue")
        btn_expert.pack(pady=5, fill=tk.X, padx=50)
        add_tooltip(btn_expert, "Aktiviert nutzlose Funktionen mit Stil")

        btn_exit = tk.Button(self.root, text="Programm beenden", command=self._handle_sarcastic_exit_prompt)
        btn_exit.pack(pady=15, fill=tk.X, padx=50) # Mehr pady oben
        add_tooltip(btn_exit, "Funktionalität entfernt")
    
    def _bind_events(self):
        """Bindet Tastenkombinationen an spezifische Aktionen."""
        self.root.bind('<Control-b>', lambda event: self.action_handler.menu_show_easter_egg(self.root))
        self.root.bind('<Control-e>', self._event_expert_mode_toggle)
        self.root.bind('<Control-q>', self._event_dev_exit)
        self.root.bind('<Control-x>', self._event_dev_exit)
        self.root.bind('<Control-s>', lambda event: self.action_handler.show_secrets(self.root))
        self.root.bind('<Alt-b>', lambda event: self.action_handler.menu_show_easter_egg(self.root))
        self.root.bind('<Alt-e>', self._event_expert_mode_toggle)
        self.root.bind('<Alt-q>', self._event_dev_exit)
        self.root.bind('<Alt-x>', self._event_dev_exit)
        self.root.bind('<Alt-s>', lambda event: self.action_handler.show_secrets(self.root))

    # --- Button Actions & Event Handlers ---
    # Die einfachen Button-Aktionen sind jetzt Lambdas, die actions.*(self.root) aufrufen

    def _action_dont_panic(self):
        """
        Aktion für den "Don't Panic!"-Button.
        Ruft die entsprechende Methode im ActionHandler auf.
        """
        # Ruft die Methode des ActionHandlers auf
        self.action_handler.dont_panic(self.root)

    def _handle_sarcastic_exit_prompt(self):
        """Startet eine Serie von sarkastischen Abfragen, bevor das Programm (eventuell) beendet wird."""

        # Setzen der Anzahl der Wiederholungen auf zufällig zwischen 2 und 5
        repetitions = random.randint(2, 5)
        
        previous_response = None  # Variable, um die vorherige Antwort zu speichern
        
        # Wiederhole die Abfragen
        for _ in range(repetitions):
            # Wähle eine zufällige Antwort, die nicht dieselbe ist wie die vorherige
            response = random.choice([r for r in constants.exit_responses if r != previous_response])
            previous_response = response
            
            if not messagebox.askretrycancel("Beenden?", response, parent=self.root):
                return  # Benutzer hat Abbrechen gewählt
        
        # Letzte Warnung, bevor die Selbstzerstörungssequenz ausgelöst wird
        confirm = messagebox.askyesno("Letzte Warnung", "Selbstzerstörungssequenz einleiten?", parent=self.root)
        if confirm:
            self.dialog_factory.create_sarcastic_countdown_dialog(self.root, exit_exception_callback=self._handle_exit_exception)
    
    def _action_show_progress(self):
        """Zeigt den Dialog für die "sinnfreie Systemanalyse"."""
        self.dialog_factory.create_show_progress_dialog(self.root)

    def _action_confirm_expert_mode(self):
        """Fragt den Benutzer, ob der "GOD-Mode" aktiviert werden soll und führt entsprechende Aktionen aus."""
        snd = DAUSound()
        warning_icon = random.choice(constants.warning_icons)
        result = messagebox.askyesno("GOD-Mode aktivieren", 
                                     f"{warning_icon} Echt jetzt?\nSind Sie ganz sicher was Sie da tun? 🤔",
                                     parent=self.root)
        if result:
            self._action_show_progress() # Zeige den "Analyse"-Fortschrittsbalken
            snd.play_drama()
            messagebox.showwarning("Hinweis", "Sie haben jetzt Zugriff auf sinnlose Optionen auf höchstem Niveau.", parent=self.root)
        else:
            snd.play_ok()
            messagebox.showinfo("Puuh...", "Das war knapp...\nSie sind nicht Gott!", parent=self.root)

    def _event_expert_mode_toggle(self, event=None): # Wird durch Ctrl+E ausgelöst
        """Event-Handler zum Umschalten des Expertenmodus (via Tastenkombination)."""
        self._action_confirm_expert_mode()

    def _event_dev_exit(self, event=None): # Wird durch Ctrl+Q ausgelöst
        """Event-Handler für den "Entwickler-Exit" (via Tastenkombination), beendet die Anwendung sofort."""
        snd = DAUSound()
        os_name, distro = get_os_details()
        msg = f"💀 Exitus Developus aktiviert auf {os_name}-System\n\n"

        if os_name == "Linux":
            msg += f"🐧 DAU auf Linux detected – Distro: {distro if distro else 'Unbekannt'}"
        elif os_name == "Windows":
            msg += "🪟 OS für DAUs. Was zu erwarten war..."
        elif os_name == "Darwin": # macOS
            msg += "🍏 Auf einem Mac? Dann ist der Fehler definitiv teuer."
        else:
            msg += "🤖 Unbekanntes Betriebssystem – gute Reise ins Daten-Nirwana."

        messagebox.showwarning("Exitus Developus", msg, parent=self.root)
        snd.play_beam()
        self.root.destroy()

    def _action_fake_optimization(self):
        """
        Startet den "Fake-Optimierungsprozess".
        Das Verhalten unterscheidet sich je nach Betriebssystem.
        """
        os_name, _ = get_os_details()
        if os_name == "Linux":
            messagebox.showwarning("Warum?", "Sinnloser als diese Software!\nAuf der richtigen Seite des Kernels du bist. 🧙‍♂️", parent=self.root)
            return
        elif os_name == "Windows":
            confirm = messagebox.askyesno("Systemoptimierung", "Oha, das dauert einen Moment!\nMöchtest du fortfahren?", parent=self.root)
            if not confirm:
                messagebox.showinfo("Abgebrochen", "Vielleicht besser so. 😉", parent=self.root)
                return
            messagebox.showinfo("Hinweis", "Du wolltest es so...\nEinen Moment bitte. Computer nicht ausschalten!", parent=self.root)
            # Starte die Fake-Optimierung in einem Thread, um die GUI nicht zu blockieren
            threading.Thread(target=self.dialog_factory.run_fake_optimization_steps_dialog, args=(self.root, self._handle_exit_exception), daemon=True).start()
        else: # macOS oder andere
             messagebox.showinfo("Systemoptimierung", "Dein System ist bereits perfekt... oder so. 😉", parent=self.root)

    # --- Methoden zum Aufrufen der ausgelagerten Dialoge ---
    def _call_sidefx_dialog(self):
        """Ruft den Dialog für den "Beipackzettel" auf."""
        self.dialog_factory.create_sidefx_dialog(self.root, self._handle_exit_exception)

    def _call_warning_dialog(self):
        """
        Ruft den "ACHTUNG!!!"-Dialog auf.
        Übergibt notwendige Callbacks für die Buttons im Dialog.
        """
        # Die Callbacks für die Buttons im Warning-Dialog müssen als Methodenreferenzen
        # oder Lambdas übergeben werden, die die Aktionen ausführen.
        self.dialog_factory.create_warning_dialog(
            parent=self.root,
            exit_exception_callback=self._handle_exit_exception,
            random_excuse_callback=lambda: self.action_handler.random_excuse(self.root),
            sidefx_callback=self._call_sidefx_dialog, # Ruft den "Beipackzettel"-Dialog auf
            dont_panic_callback=self._action_dont_panic
        )