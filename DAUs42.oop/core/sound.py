"""
Modul zur plattformunabhängigen Wiedergabe von Soundeffekten für die DAUs42-Anwendung.
Verwendet unterschiedliche Systembefehle oder Bibliotheken je nach Betriebssystem.
"""
import os
import pathlib
import platform
import tkinter.messagebox as messagebox

class DAUSound:
    """
    Eine Klasse zur Kapselung der Soundwiedergabe-Logik.
    Bietet einfache Methoden zum Abspielen vordefinierter Sounds.
    """
    def __init__(self):
        """Initialisiert das DAUSound-Objekt."""
        # Derzeit keine spezielle Initialisierung erforderlich.
        
    def play_alarm(self):
        self.play_snd("alarm.wav")

    def play_beam(self):
        self.play_snd("beam.wav")

    def play_beam2(self):
        self.play_snd("beam2.wav")

    def play_drama(self):
        self.play_snd("drama.wav")

    def play_ok(self):
        self.play_snd("ok.wav")

    @staticmethod
    def play_snd(sndfile_name):
        """ Spielt eine Sounddatei ab, abhängig vom Betriebssystem. """
        # Annahme: Dieses Skript ist in core/, assets/ ist eine Ebene höher.
        ASSETS_BASE_DIR = pathlib.Path(__file__).resolve().parent.parent / "assets"

        filepath = ASSETS_BASE_DIR / sndfile_name

        if not filepath.exists():
            messagebox.showinfo("Datei nicht gefunden", f"⚠ Sounddatei '{filepath}' wurde nicht gefunden.")
            return

        os_name = platform.system()

        try:
            if os_name == "Windows":
                import winsound
                winsound.PlaySound(str(filepath), winsound.SND_FILENAME | winsound.SND_ASYNC)
            elif os_name == "Darwin": # macOS
                os.system(f"afplay -q '{filepath}' &")
            elif os_name == "Linux":
                os.system(f"aplay -q '{filepath}' &")
            else:
                messagebox.showinfo("Nicht unterstützt", "Sound-Ausgabe wird auf diesem System nicht unterstützt.")
        except Exception as e:
            messagebox.showerror("Fehler", f"Sound konnte nicht abgespielt werden:\n{e}")