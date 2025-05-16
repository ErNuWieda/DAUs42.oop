"""
Behandelt Aktionen, die durch Benutzerinteraktionen (Buttons, Menüs) ausgelöst werden.
Diese Klasse kapselt die Logik für verschiedene "sinnfreie" Operationen der Anwendung.
"""
import random
from tkinter import messagebox
from . import constants
from .constants import t
from .sound import DAUSound

class ActionHandler:
    """
    Verwaltet und führt Aktionen aus, die von der UI ausgelöst werden.
    Nutzt DAUSound für Soundeffekte und constants für Textnachrichten.
    """
    def __init__(self, lang):
        """Initialisiert den ActionHandler mit einem SoundPlayer und System-Sprache."""
        self.lang = lang
        self.previous_status = None
        self.previous_response = None
        self.previous_quote = None
        self.previous_excuse = None
        self.sound_player = DAUSound()

    # --- Secret Action ---
    def show_secrets(self, parent):
        """Zeigt eine Informationsbox mit geheimen Tastenkombinationen an."""
        if self.lang == "de":
            title = "Geheime Tastenkombinationen"
            text = "[Alt|Strg]+B Easter Egg finden\n[Alt|Strg]+E GOD-Mode\n[Alt|Strg]+S gerade entdeckt\n[Alt|Strg]+[Q|X] Beenden\n\nGibt's noch mehr? 🤔"
        else:
            title = "Secret keyboard shortcuts"
            text = "[Alt|Ctrl]+B Find Easter Egg\n[Alt|Ctrl]+E GOD Mode\n[Alt|Ctrl]+S Just discovered\n[Alt|Ctrl]+[Q|X] Exit\n\nIs there more? 🤔"
        messagebox.showinfo(title, text, parent=parent)

    # --- Button Actions ---
    def print_internet(self, parent):
        """
        Simuliert das Drucken des Internets.
        Zeigt eine zufällige Statusmeldung aus constants.internet_status an.
        """
        # Um Wiederholungen über mehrere Aufrufe hinweg zu vermeiden, ist `previous_status`
        # ein Instanzattribut
        status = random.choice([r for r in constants.internet_status[self.lang].values() if r != self.previous_status])
        self.previous_status = status
        if self.lang == "de":
            messagebox.showinfo("Internetdruck", status, parent=parent)
        else:
            messagebox.showinfo("Internet print", status, parent=parent)


    def dau_console(self, parent):
        """Zeigt eine zufällige, sarkastische Antwort für "DAUs" an."""
        response = random.choice([r for r in constants.dau_responses[self.lang].values() if r != self.previous_response])
        self.previous_response = response
        if self.lang == "de":
            messagebox.showinfo("DAUs Konsole", response, parent=parent)
        else:
            messagebox.showinfo("DAU-console", response, parent=parent)

    def ultimate_answer(self, parent):
        """Zeigt eine zufällige "ultimative Antwort" oder ein Zitat zum Thema 42 an."""
        quote = random.choice([r for r in constants.random_quotes[self.lang].values() if r != self.previous_quote])
        self.previous_quote = quote
        if self.lang == "de":
            messagebox.showinfo("Ultimative Antwort", quote, parent=parent)
        else:
            messagebox.showinfo("Ultimate Answer", quote, parent=parent)

    def random_excuse(self, parent):
        """Zeigt eine zufällige Ausrede an."""
        excuse = random.choice([r for r in constants.excuses[self.lang].values() if r != self.previous_excuse])
        self.previous_excuse = excuse
        if self.lang == "de":
            messagebox.showinfo("Zufällige Ausrede", excuse, parent=parent)
        else:
            messagebox.showinfo("Random Excuse", excuse, parent=parent)


    def dont_panic(self, parent):
        """Zeigt ein beruhigendes Zitat an und spielt einen Soundeffekt."""
        quote = random.choice([r for r in constants.calming_quotes[self.lang].values() if r != self.previous_quote])
        self.previous_quote = quote
        messagebox.showinfo("Don't Panic!", quote, parent=parent)
        self.sound_player.play_ok()

    # --- Menu Actions ---
    def menu_show_sinnlosigkeit(self, parent):
        """Aktion für den Menüpunkt "Neue Sinnlosigkeit"."""
        if self.lang == "de":
            title = "Sinnlosigkeit"
            text = "Ein neues Maß an Bedeutungslosigkeit wurde erreicht."
        else:
            title = "Futility"
            text = "A new level of insignificance has been reached."
        messagebox.showinfo(title, text, parent=parent)

    def menu_show_undo_too_late(self, parent):
        """Aktion für den Menüpunkt "Alles rückgängig machen"."""
        if self.lang == "de":
            text = "Zu spät. Der Kaffee ist bereits verschüttet."
        else:
            text = "Too late. The coffee is already scrambled."
        messagebox.showinfo("Undo", text, parent=parent)

    def menu_show_invisible_options_error(self, parent):
        """Aktion für den Menüpunkt "Unsichtbare Optionen anzeigen"."""
        if self.lang == "de":
            text = "Fehler 401: Unsichtbarkeit nicht autorisiert."
        else:
            text = "Error 401: Invisibility not authorized."
        messagebox.showinfo("Oops", text, parent=parent)

    def menu_do_nothing_warning(self, parent):
        """Aktion für den Menüpunkt "Nichts tun"."""
        if self.lang == "de":
            messagebox.showwarning("Meta-Warnung", "Du hast erfolgreich... nichts getan.", parent=parent)
        else:
            messagebox.showwarning("Meta-Warning", "You have successfully... done nothing.", parent=parent)
        

    def menu_show_help_purpose(self, parent):
        """Aktion für den Menüpunkt "Was soll das alles?" im Hilfe-Menü."""
        if self.lang == "de":
            messagebox.showinfo("Hilfe", "Diese Software verfolgt keinerlei Zweck.\nUnd das ist auch gut so.", parent=parent)
        else:
            messagebox.showinfo("Help", "This software serves no purpose whatsoever.\nAnd that's a good thing.", parent=parent)


    def menu_show_easter_egg(self, parent):
        """Aktion für den Menüpunkt "Easter Egg finden". Spielt auch einen Sound."""

        if self.lang == "de":
            msg = "Glückwunsch!\nDu hast das Sinnfreiheits-Level 9000 erreicht!\n\n🎉 Bonus: 1 virtueller Keks 🍪"
        else:
            msg = "Congratulations!\nYou have reached the meaningless level 9000!\n\n🎉 Bonus: 1 virtual cookie 🍪"

        messagebox.showinfo("🐇 Easter Egg", msg, parent=parent)
        self.sound_player.play_beam2()

    def menu_show_about(self, parent):
        """Zeigt den "Über"-Dialog an. Spielt auch einen Sound."""
        self.sound_player.play_beam2()
        if self.lang == "de":
            title = "Über DAUs forty-two"
            text = "🧠 Version: 42.0.∞\n☕ Make Bash not War\n🕒 Uptime seit Kaffee Nr. 3\n\n© 2025-∞ airnooweeda"
        else:
            title = "About DAUs forty-two"
            text = "🧠 Version: 42.0.∞\n☕ Make Bash not War\n🕒 Uptime since Coffee Nr. 3\n\n© 2025-∞ airnooweeda"
        messagebox.showinfo(title, text, parent=parent)
