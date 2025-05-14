"""
Modul für den Fake-Installationsprozess der DAUs42-Anwendung.
Simuliert eine Installation mit humorvollen Schritten und einer kleinen Animation.
"""
import tkinter as tk
from tkinter import Toplevel, Label, Button, messagebox
from PIL import Image, ImageTk
import pathlib
import os

class DAUFakeInstaller():
    """
    Simuliert einen Installationsprozess für die DAUs42-Anwendung.

    Zeigt ein Fenster mit einer Animation und fiktiven Installationsschritten an,
    bevor die eigentliche Hauptanwendung gestartet wird.
    """
    def __init__(self, root_tk_instance):
        """Initialisiert das Fake-Installationsfenster."""
        self.root = root_tk_instance
        self.install_window = tk.Toplevel(self.root)
        self.install_window.title("Installiere galaktische Systemkomponenten...")
        self.install_window.geometry("400x200")
        self.install_window.resizable(False, False)
        # Stellt sicher, dass das Installationsfenster im Vordergrund ist
        self.install_window.attributes('-topmost', 'true')
        self.install_window.focus_force() 
        self.install_window.protocol("WM_DELETE_WINDOW", lambda: None)
        self.marvins_pic = self._load_picture("marvin.png")
        self._show_picture()

    def _load_picture(self, picture_name):
        """
        Lädt ein Bild aus dem Assets-Ordner.

        Args:
            picture_name (str): Der Dateiname des Bildes.

        Returns:
            PIL.Image.Image: Das geladene Bildobjekt.
        """
        picture = "../assets"+os.sep+picture_name
        filepath = pathlib.Path(__file__).parent / picture
        bild = Image.open(filepath)

        return bild

    def _show_picture(self):
        """Zeigt das geladene Bild (Marvin) im Installationsfenster an."""

        im_tk = ImageTk.PhotoImage(self.marvins_pic)
        self.pic_label = tk.Label(self.install_window, image=im_tk)
        self.pic_label.image = im_tk
        self.pic_label.pack()


# DAUApp wird später importiert, um zirkuläre Abhängigkeiten zu vermeiden, falls nötig.
# from .app import DAUApp
    def start_installation(self, on_complete_callback=None):
        """
        Zeigt ein Fake-Installationsfenster an und startet dann die Hauptanwendung.
        Ruft on_complete_callback auf, wenn die "Installation" abgeschlossen ist.
        """
        self.on_complete_callback = on_complete_callback

        install_label = Label(self.install_window, text="Initialisiere...", font=("Arial", 14))
        install_label.pack(padx=20, pady=20)

        install_steps = [
            "Handtuch", "Babelfisch", "Sub-Etha-Sender",
            "Vogonen-Poesie-Modul", "Unwahrscheinlichkeits-Drive", "Deep Thought KI", 
            "geheime Tastenkombinationen", "Sarkasmus-Modul V2"
        ]
        
        num_steps = len(install_steps)
        segment_angle = 360 / num_steps if num_steps > 0 else 0

        def do_install_step(index=0):
            """
            Führt einen einzelnen "Installationsschritt" aus.

            Args:
                index (int): Der Index des aktuellen Installationsschritts.
            """
            if index < num_steps:
                angle = (index + 1) * segment_angle
                im_rotated = self.marvins_pic.rotate(angle, fillcolor="white")
                im_tk = ImageTk.PhotoImage(im_rotated)
                self.pic_label.config(image=im_tk)
                self.pic_label.image = im_tk # Referenz behalten
                install_label.config(text=f"Installiere {install_steps[index]}...")
                
                # UI aktualisieren erzwingen, bevor die Pause beginnt (optional, aber kann helfen)
                # self.install_window.update_idletasks() 
                
                # Ersetze time.sleep(0.8) durch eine nicht-blockierende Pause mit after()
                # Die nächste Aktion (schedule_next_install_step) wird nach 800ms aufgerufen.
                self.install_window.after(800, lambda: schedule_next_install_step(index))
            else:
                # Alle Schritte abgeschlossen
                messagebox.showinfo("Installation abgeschlossen", 
                                    "Alle absurden Erweiterungen erfolgreich installiert!", 
                                    parent=self.install_window)
                if self.on_complete_callback:
                    self.on_complete_callback()
                
                # Fenster nach einer weiteren kurzen Verzögerung zerstören
                self.install_window.after(500, self.install_window.destroy)  

        def schedule_next_install_step(current_index):
            """
            Plant den nächsten Installationsschritt nach einer kurzen Verzögerung.
            Dies hilft, die UI reaktionsfähig zu halten.
            Args:
                current_index (int): Der Index des gerade abgeschlossenen Schritts.
            """
            # Planen des nächsten eigentlichen Installationsschritts nach einer kurzen Verzögerung (50ms)
            self.install_window.after(50, lambda: do_install_step(current_index + 1))

        # Starte den Installationsprozess
        # Kurze initiale Verzögerung, damit das Fenster korrekt gezeichnet wird
        self.install_window.after(100, lambda: do_install_step(0))