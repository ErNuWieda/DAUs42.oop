"""
Modul zur Erstellung verschiedener thematischer Dialogfenster für die DAUs42-Anwendung.
Enthält eine DialogFactory-Klasse, die Methoden zur Erzeugung spezifischer Dialoge bereitstellt.
"""
import tkinter as tk
from tkinter import ttk, messagebox, Toplevel, Label, Button
from PIL import Image, ImageTk
import os
import pathlib
import random
from .sound import DAUSound
from . import constants # Zugriff auf Konstanten
from .constants import t, sidefx_texts, warning_dialog_texts



class DialogFactory:
    """
    Eine Factory-Klasse zum Erstellen verschiedener spezialisierter Dialogfenster.
    Jede Methode erstellt und konfiguriert einen bestimmten Dialogtyp.
    """
    def __init__(self, lang):
        """Initialisiert die DialogFactory mit einer Instanz von DAUSound."""
        self.lang = lang
        self.sound_player = DAUSound() # Zentrale Sound-Instanz für Dialoge


    def _load_dlgbg(self, dlg, bg_name):
        """
        Lädt ein Hintergrundbild für einen Dialog und passt es an die Dialoggröße an.
        Args:
            dlg (Toplevel): Das Dialogfenster, für das das Bild geladen wird.
            bg_name (str): Der Dateiname des Bildes im 'assets'-Ordner.
        Returns:
            ImageTk.PhotoImage: Das für Tkinter vorbereitete Bildobjekt.
        """
        ASSETS_BASE_DIR = pathlib.Path(__file__).resolve().parent.parent / "assets"
        filepath = ASSETS_BASE_DIR / bg_name
        dlg.update_idletasks() # Sicherstellen, dass die Fenstergröße bekannt ist
        bild = Image.open(filepath)
        bild = bild.resize((dlg.winfo_width(), dlg.winfo_height()))
        bild_tk = ImageTk.PhotoImage(bild)
        return bild_tk

    def show_vogon_poetry(self, parent, exit_exception_callback):
        poetry_dialog = Toplevel(parent)
        if self.lang == "de":
            poetry_dialog.title("Vogon-Poesie")
        else:
            poetry_dialog.title("Vogon Poetry")
        poetry_dialog.geometry("800x400")
        poetry_dialog.resizable(False, False)
        # Verhindert das Schließen über den X-Button
        poetry_dialog.protocol("WM_DELETE_WINDOW", exit_exception_callback) 
        poetry_dialog.attributes('-topmost', 'true')
        poetry_dialog.focus_force()

        dialog_width = 800
        dialog_height = 400

    # Canvas erstellen, der das gesamte Dialogfenster ausfüllt
        canvas = tk.Canvas(poetry_dialog, width=dialog_width, height=dialog_height, highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        bg_image = self._load_dlgbg(poetry_dialog, "vogon_poetry.jpg") # self._load_dlgbg verwenden
        # Bild auf den Canvas zeichnen (zentriert)
        canvas.create_image(dialog_width/2, dialog_height/2, image=bg_image)
        canvas.image = bg_image # Wichtig: Referenz auf das Bild halten!

        y_offset = 20 # Initialer Y-Versatz von oben

        ok_button = Button(poetry_dialog, text="🤪  OMG  🤪", 
                           command=poetry_dialog.destroy, 
                           fg="cyan", bg="magenta", relief="raised", padx=10, pady=5)
        
        button_y_pos = y_offset+340 # Position nach dem letzten Text
        canvas.create_window(
            dialog_width / 2, button_y_pos,
            window=ok_button,
            anchor="n"
        )
        
    def create_sarcastic_countdown_dialog(self, parent, exit_exception_callback=None):
        """
        Erstellt und startet einen sarkastischen Countdown-Dialog, der eine "Selbstzerstörung" simuliert.

        Args:
            parent (tk.Widget): Das übergeordnete Widget für diesen Dialog.
            exit_exception_callback (callable, optional): Callback-Funktion, die aufgerufen wird,
                wenn versucht wird, das Fenster über den Schließen-Button zu schließen.
        Returns:
            Toplevel: Das erstellte Countdown-Dialogfenster.
        """
        # soundman = DAUSound() # Wird jetzt über self.sound_player genutzt
        timer_duration = random.randint(5, 10)
        
        countdown_window = Toplevel(parent)
        countdown_window.resizable(False, False)
        countdown_window.protocol("WM_DELETE_WINDOW", exit_exception_callback)
        if self.lang == "de":
            title = "Selbstzerstörung"
        else:
            title = "Self-Destruction"
        countdown_window.title(title)
        
        countdown_label = Label(countdown_window, text=f"{title} in {timer_duration}", font=("Courier", 18), fg="red")
        countdown_label.pack(padx=20, pady=20)
        
        countdown_bar = ttk.Progressbar(countdown_window, orient='horizontal', length=250, mode='determinate', maximum=timer_duration)
        countdown_bar.pack(pady=10)
        countdown_bar['value'] = timer_duration

        def countdown(n):
            """
            Führt einen einzelnen Schritt des Countdowns aus und aktualisiert die UI.
            Ruft sich selbst rekursiv über `after` auf, bis der Countdown abgelaufen ist.

            Args:
                n (int): Die verbleibende Anzahl an Sekunden im Countdown.
            """
            bomb_states = ["💣", "🧨", "💥"]
            current_bomb = bomb_states[n % len(bomb_states)]
            colors = ["red", "orange", "gold"]
            current_color = colors[n % len(colors)]

            if n > 0:
                if self.lang == "de":
                    text=f"{current_bomb} noch {n} Sekunden bis CPU-Meltdown..."
                else:
                    text=f"{current_bomb} {n} seconds remaining to CPU-Meltdown..."
                countdown_label.config(text=text, font=("Courier", 18), fg=current_color)
                countdown_bar['value'] = n
                self.sound_player.play_alarm()
                countdown_window.after(1000, lambda current_n=n: countdown(current_n - 1)) # Korrigiertes Lambda für after
            else:
                if self.lang == "de":
                    text="💥 Zerstörung abgebrochen.\nDrücken Sie nie wieder diesen Knopf! 💀"
                else:
                    text="💥 Destruction aborted.\nDon't press this button again! 💀"
                countdown_label.config(text=text, fg="red", bg="gold")
                countdown_bar['value'] = n+1            
                countdown_window.after(4000, countdown_window.destroy)
                
        countdown(timer_duration)
        return countdown_window

    def create_show_progress_dialog(self, parent):
        """
        Erstellt einen Dialog, der eine "sinnfreie Systemanalyse" mit einem unbestimmten Fortschrittsbalken simuliert.

        Args:
            parent (tk.Widget): Das übergeordnete Widget für diesen Dialog.

        Returns:
            Toplevel: Das erstellte Fortschrittsdialogfenster.
        """
        progress_dialog = Toplevel(parent)
        progress_dialog.geometry("300x100")
        progress_dialog.resizable(False, False)
        if self.lang == "de":
            progress_dialog.title("Systemanalyse")
        else:
            progress_dialog.title("System Analysis")
    
        label = Label(progress_dialog, text=progress_dialog.title(), font=("Courier", 14))
        label.pack(pady=10)

        bar = ttk.Progressbar(progress_dialog, orient='horizontal', length=250, mode='indeterminate')
        bar.pack(pady=5)
        bar.start(10)

        def finish_progress():
            """Beendet den Fortschrittsbalken, zeigt eine Abschlussmeldung und schließt den Dialog."""
            bar.stop()
            self.sound_player.play_ok()
            if self.lang == "de":
                title = "Ergebnis"
                text = "Analyse abgeschlossen: Alles ist sinnlos – wie erwartet."
            else:
                title = "Result"
                text = "Analyse completed: Everything is meaningless – as expected."
            messagebox.showinfo(title, text, parent=progress_dialog)
            progress_dialog.destroy()

        progress_dialog.after(5000, finish_progress)
        return progress_dialog

    def run_fake_optimization_steps_dialog(self, parent, exit_exception_callback):
        """
        Zeigt einen Dialog an, der eine Reihe von "Fake-Optimierungsschritten" durchläuft.
        Dieser Dialog ist modal und blockiert andere Interaktionen, bis er abgeschlossen ist.

        Args:
            parent (tk.Widget): Das übergeordnete Widget für diesen Dialog.
            exit_exception_callback (callable): Callback-Funktion für das Schließen-Event des Fensters
                                                (hier deaktiviert durch `lambda: None`).
        Returns:
            Toplevel: Das erstellte Dialogfenster für die Optimierungsschritte.
        """
        steps = constants.fake_optimization_steps # Ausgelagerte Schritte

        step_window = Toplevel(parent)
        if self.lang == "de":
            step_window.title("Systemoptimierung")
        else:
            step_window.title("System Optimization")
        step_window.geometry("500x150")
        step_window.configure(bg="black")
        self.sound_player.play_drama()
        step_window.grab_set() # Macht den Dialog modal
        step_window.protocol("WM_DELETE_WINDOW", lambda: None) # Verhindert das Schließen über den X-Button
        label = Label(step_window, text="", fg="lime", bg="black", font=("Courier", 14))
        label.pack(pady=30)

        def show_step(index=0):
            """
            Zeigt einen einzelnen Optimierungsschritt an und plant den nächsten.

            Args:
                index (int): Der Index des aktuell anzuzeigenden Schritts.
            """
            if index < len(steps):
                label.config(text=steps[index])
                step_window.update() 
                step_window.after(2500, lambda current_idx=index: show_step(current_idx + 1)) # Korrigiertes Lambda
            else:
                step_window.destroy()
                if self.lang == "de":
                    text = "War nur Spaß!\n\nKeine Sorge, dein System ist sicher."
                else:
                    text = "Just kidding!\n\nDon't worry, your system is safe."

                messagebox.showinfo("😉", "😄😄😄😄😄\n\n"+text, parent=parent)
        
        show_step()
        return step_window

    def create_sidefx_dialog(self, parent, exit_exception_callback):
        """
        Erstellt den "Beipackzettel"-Dialog mit humorvollen Nebenwirkungen und Hinweisen.
        Der Dialog verwendet ein Hintergrundbild und platziert Texte sowie einen Button auf einem Canvas.

        Args:
            parent (tk.Widget): Das übergeordnete Widget für diesen Dialog.
            exit_exception_callback (callable): Callback-Funktion, die aufgerufen wird,
                wenn versucht wird, das Fenster über den Schließen-Button zu schließen.
        Returns:
            Toplevel: Das erstellte "Beipackzettel"-Dialogfenster.
        """
        sidefx_dialog = Toplevel(parent)
        if self.lang == "de":
            sidefx_dialog.title("Hinweise zur sinnfreien Anwendung von DAUs forty-two")
        else:
            sidefx_dialog.title("Hints for meaningless use of DAUs forty-two")
        sidefx_dialog.geometry("540x675")
        sidefx_dialog.resizable(False, False)
        sidefx_dialog.protocol("WM_DELETE_WINDOW", exit_exception_callback)
        sidefx_dialog.attributes('-topmost', 'true')
        sidefx_dialog.focus_force()

        # Feste Dialogdimensionen verwenden, die in geometry() gesetzt wurden
        dialog_width = 540
        dialog_height = 675

        # Canvas erstellen, der das gesamte Dialogfenster ausfüllt
        canvas = tk.Canvas(sidefx_dialog, width=dialog_width, height=dialog_height, highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        bg_image = self._load_dlgbg(sidefx_dialog, "milkyway.jpg") # self._load_dlgbg verwenden
        # Bild auf den Canvas zeichnen (zentriert)
        canvas.create_image(dialog_width/2, dialog_height/2, image=bg_image)
        canvas.image = bg_image # Wichtig: Referenz auf das Bild halten!

        y_offset = 20 # Initialer Y-Versatz von oben

        # Textkonfigurationen: (key, font, color, y_increment, anchor, justify, x_pos, width_factor)
        # x_pos: absolute X-Position für den Ankerpunkt
        # width_factor: Anteil der Dialogbreite für den Textumbruch
        text_configs = [
            # Key, Font, Color, Y-Increment, Anchor, Justify, X-Pos, Width-Factor
            ("lbl1", ("Helvetica", 10), "white", 65, "n", "center", dialog_width / 2, 0.9),
            ("lbl2", ("Helvetica", 10, "italic"), "lightgray", 45, "n", "center", dialog_width / 2, 0.9),
            ("lbl5_title", ("Helvetica", 12, "bold"), "lightgreen", 20, "n", "center", dialog_width / 2, 0.9),
            ("lbl6_effects", ("Helvetica", 9), "white", 75, "nw", "left", dialog_width * 0.05, 0.9),
            ("lbl3_title", ("Helvetica", 12, "bold"), "orange", 20, "n", "center", dialog_width / 2, 0.9),
            ("lbl4_effects", ("Helvetica", 9), "white", 75, "nw", "left", dialog_width * 0.05, 0.9),
            ("lbl7_title", ("Helvetica", 12, "bold"), "red", 20, "n", "center", dialog_width / 2, 0.9),
            ("lbl8_effects", ("Helvetica", 9), "white", 130, "nw", "left", dialog_width * 0.05, 0.9),
            ("lbl9_advice", ("Helvetica", 10, "italic"), "gold", 70, "n", "center", dialog_width / 2, 0.9),
        ]

        for key, font, color, dy, anchor, justify, x_pos, width_factor in text_configs:
            text_content = t(sidefx_texts, self.lang, key)
            text_wrap_width = int(dialog_width * width_factor)
            
            canvas.create_text(
                x_pos, y_offset,
                text=text_content,
                font=font,
                fill=color,
                anchor=anchor,
                justify=justify,
                width=text_wrap_width
            )
            y_offset += dy

        # Button erstellen und auf dem Canvas platzieren
        if self.lang == "de":
            text = "Mir doch egal"
        else:
            text = "I don't care"
        ok_button = Button(sidefx_dialog, text=text, 
                           command=sidefx_dialog.destroy, 
                           bg="lightgrey", relief="raised", padx=10, pady=5)
        
        button_y_pos = y_offset+75 # Position nach dem letzten Text
        canvas.create_window(
            dialog_width / 2, button_y_pos,
            window=ok_button,
            anchor="n"
        )
        return sidefx_dialog

    def create_warning_dialog(self, parent, exit_exception_callback, random_excuse_callback, sidefx_callback, dont_panic_callback):
        """
        Erstellt den "ACHTUNG!!!"-Dialog mit wichtigen (und weniger wichtigen) Warnungen.
        Dieser Dialog verwendet ebenfalls ein Hintergrundbild auf einem Canvas und platziert
        Texte sowie eine Reihe von Buttons mit verschiedenen Aktionen.

        Args:
            parent (tk.Widget): Das übergeordnete Widget für diesen Dialog.
            exit_exception_callback (callable): Callback für das Schließen-Event des Fensters.
            random_excuse_callback (callable): Callback für Buttons, die eine zufällige Ausrede anzeigen.
            sidefx_callback (callable): Callback, um den "Beipackzettel"-Dialog anzuzeigen.
            dont_panic_callback (callable): Callback für den "Don't Panic"-Button.
        Returns:
            Toplevel: Das erstellte Warnungs-Dialogfenster.
        """
        warning_dialog = Toplevel(parent)
        if self.lang == "de":
            warning_dialog.title("ACHTUNG!!!")
        else:
            warning_dialog.title("ATTENTION!!!")
        warning_dialog.geometry("540x300")
        warning_dialog.resizable(False, False)
        warning_dialog.protocol("WM_DELETE_WINDOW", exit_exception_callback)
        warning_dialog.attributes('-topmost', 'true')
        warning_dialog.focus_force()

        # Canvas erstellen, der das gesamte Dialogfenster ausfüllt
        canvas = tk.Canvas(warning_dialog, width=540, height=300, highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        bg_image = self._load_dlgbg(warning_dialog, "vogon.png") # self._load_dlgbg verwenden
        # Bild auf den Canvas zeichnen (zentriert)
        canvas.create_image(540/2, 300/2, image=bg_image)
        canvas.image = bg_image # Wichtig: Referenz auf das Bild halten!

        # Texte direkt auf den Canvas zeichnen
        # Die y-Positionen müssen ggf. angepasst werden für ein schönes Layout
        y_offset = 30
        canvas.create_text(50, y_offset, text="⚠️", font=("Helvetica", 40), fill="yellow", anchor="w")
        canvas.create_text(110, y_offset - 5 , text=t(warning_dialog_texts, self.lang, "main_warning"), font=("Helvetica", 14), fill="red", anchor="w")
        canvas.create_text(warning_dialog.winfo_width() - 70, y_offset, text="⚠️", font=("Helvetica", 40), fill="yellow", anchor="w")

        y_offset += 60 # Nächste Zeile
        text_items = [
            (t(warning_dialog_texts, self.lang, "vogon_offices"), "lightgray"),
            (t(warning_dialog_texts, self.lang, "pan_galactic_gargle_blaster"), "blue"),
            (t(warning_dialog_texts, self.lang, "no_towel"), "lightgreen"),
            (t(warning_dialog_texts, self.lang, "babel_fish_fired"), "orange"),
            (t(warning_dialog_texts, self.lang, "answer_unknown"), "violet"),
       ]

        for text, color in text_items:
            canvas.create_text(warning_dialog.winfo_width()/2, y_offset, text=text, font=("Helvetica", 13), fill=color, anchor="center")
            y_offset += 25 # Abstand für die nächste Zeile

        # Button-Frame erstellen (dieser wird einen eigenen, opaken Hintergrund haben)
        if self.lang == "de":
            blu_btn_txt = "🤪 Hicks..."
            grn_btn_txt = "💀 Ich werde sterben"
        else:
            blu_btn_txt = "🤪 Hiccs..."
            grn_btn_txt = "💀 I'll die" 
        btn_frame = tk.Frame(warning_dialog, bg="black") # Dieser Frame wird auf den Canvas gelegt
        Button(btn_frame, text="😬 Aaargh!", bg="white", fg="gray", command=lambda: self.show_vogon_poetry(warning_dialog, exit_exception_callback)).pack(side=tk.LEFT, padx=2)
        Button(btn_frame, text=blu_btn_txt, bg="blue", fg="white", command=random_excuse_callback).pack(side=tk.LEFT, padx=2)
        Button(btn_frame, text=grn_btn_txt, bg="green", fg="white", command=sidefx_callback).pack(side=tk.LEFT, padx=2)
        Button(btn_frame, text="🤯 Panic!", bg="orange", fg="green", command=dont_panic_callback).pack(side=tk.LEFT, padx=2)
        Button(btn_frame, text="😎 42", bg="purple", fg="gold", command=warning_dialog.destroy).pack(side=tk.LEFT, padx=2)
        btn_frame.pack(pady=5)

        # Button-Frame auf dem Canvas platzieren
        # warning_dialog.update_idletasks() # Sicherstellen, dass btn_frame Größe hat
        # Beispiel: Rechteck (halbtransparenter Effekt durch helle Farbe)
        canvas.create_window(warning_dialog.winfo_width()/2, y_offset + 30, window=btn_frame, anchor="center")

        return warning_dialog