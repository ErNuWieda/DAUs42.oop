"""
Behandelt Aktionen, die durch Benutzerinteraktionen (Buttons, Menüs) ausgelöst werden.
Diese Klasse kapselt die Logik für verschiedene "sinnfreie" Operationen der Anwendung.
"""
import random
from tkinter import messagebox
from . import constants
from .sound import DAUSound

class ActionHandler:
    """
    Verwaltet und führt Aktionen aus, die von der UI ausgelöst werden.
    Nutzt DAUSound für Soundeffekte und constants für Textnachrichten.
    """
    def __init__(self):
        """Initialisiert den ActionHandler mit einem SoundPlayer."""
        self.sound_player = DAUSound()

    # --- Secret Action ---
    def show_secrets(self, parent):
        """Zeigt eine Informationsbox mit geheimen Tastenkombinationen an."""
        messagebox.showinfo("Geheime Tastenkombinationen", "[Alt|Strg]+B Easter Egg finden\n[Alt|Strg]+E GOD-Mode\n[Alt|Strg]+S gerade entdeckt\n[Alt|Strg]+[Q|X] Beenden\n\nGibt's noch mehr? 🤔", parent=parent)

    # --- Button Actions ---
    def print_internet(self, parent):
        """
        Simuliert das Drucken des Internets.
        Zeigt eine zufällige Statusmeldung aus constants.internet_status an.
        """
        # Hinweis: Die Logik zur Vermeidung von Wiederholungen wirkt nur innerhalb dieses einen Aufrufs.
        # Um Wiederholungen über mehrere Aufrufe hinweg zu vermeiden, müsste `previous_status`
        # ein Instanzattribut oder anderweitig persistent sein. Für den humoristischen Zweck
        # dieser Anwendung ist das aktuelle Verhalten aber vermutlich ausreichend.
        previous_status = None # Hinweis: Diese Logik verhindert Wiederholungen nur innerhalb eines Aufrufs, nicht über mehrere.
        status = random.choice([r for r in constants.internet_status if r != previous_status])
        previous_status = status
        messagebox.showinfo("Internetdruck", status, parent=parent)

    def dau_console(self, parent):
        """Zeigt eine zufällige, sarkastische Antwort für "DAUs" an."""
        previous_response = None
        response = random.choice([r for r in constants.dau_responses if r != previous_response])
        previous_response = response
        messagebox.showinfo("DAU-Konsole", response, parent=parent)

    def ultimate_answer(self, parent):
        previous_quote = None
        """Zeigt eine zufällige "ultimative Antwort" oder ein Zitat zum Thema 42 an."""
        quote = random.choice([r for r in constants.random_quotes if r != previous_quote])
        previous_quote = quote
        messagebox.showinfo("Antwort 42", quote, parent=parent)

    def random_excuse(self, parent):
        """Zeigt eine zufällige Ausrede an."""
        previous_excuse = None
        excuse = random.choice([r for r in constants.excuses if r != previous_excuse])
        previous_excuse = excuse
        messagebox.showinfo("Zufällige Ausrede", excuse, parent=parent)

    def dont_panic(self, parent):
        """Zeigt ein beruhigendes Zitat an und spielt einen Soundeffekt."""
        previous_quote = None
        quote = random.choice([r for r in constants.calming_quotes if r != previous_quote])
        previous_quote = quote
        messagebox.showinfo("Don't Panic!", quote, parent=parent)
        self.sound_player.play_ok()

    # --- Menu Actions ---
    def menu_show_sinnlosigkeit(self, parent):
        """Aktion für den Menüpunkt "Neue Sinnlosigkeit"."""
        messagebox.showinfo("Sinnlosigkeit", "Ein neues Maß an Bedeutungslosigkeit wurde erreicht.", parent=parent)

    def menu_show_undo_too_late(self, parent):
        """Aktion für den Menüpunkt "Alles rückgängig machen"."""
        messagebox.showinfo("Undo", "Zu spät. Der Kaffee ist bereits verschüttet.", parent=parent)

    def menu_show_invisible_options_error(self, parent):
        """Aktion für den Menüpunkt "Unsichtbare Optionen anzeigen"."""
        messagebox.showinfo("Oops", "Fehler 401: Unsichtbarkeit nicht autorisiert.", parent=parent)

    def menu_do_nothing_warning(self, parent):
        """Aktion für den Menüpunkt "Nichts tun"."""
        messagebox.showwarning("Meta-Warnung", "Du hast erfolgreich... nichts getan.", parent=parent)

    def menu_show_help_purpose(self, parent):
        """Aktion für den Menüpunkt "Was soll das alles?" im Hilfe-Menü."""
        messagebox.showinfo("Hilfe", "Diese Software verfolgt keinerlei Zweck.\nUnd das ist auch gut so.", parent=parent)

    def menu_show_easter_egg(self, parent):
        """Aktion für den Menüpunkt "Easter Egg finden". Spielt auch einen Sound."""
        messagebox.showinfo("🐇 Easter Egg", "Glückwunsch!\nDu hast das Sinnfreiheits-Level 9000 erreicht!\n\n🎉 Bonus: 1 virtueller Keks 🍪", parent=parent)
        self.sound_player.play_beam2()

    def menu_show_about(self, parent):
        """Zeigt den "Über"-Dialog an. Spielt auch einen Sound."""
        self.sound_player.play_beam2()
        messagebox.showinfo("Über DAUs forty-two",
                            "🧠 Version: 42.0.∞\n☕ Make Bash not War\n🕒 Uptime seit Kaffee Nr. 3\n\n© 2025-∞ airnooweeda",
                            parent=parent)