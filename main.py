"""
Haupt-Startskript für die DAUs42-Anwendung.

Dieses Skript initialisiert die Tkinter-Hauptinstanz, startet den Fake-Installer
und anschließend die Hauptanwendung DAUApp.
"""
import tkinter as tk
from core.app import DAUApp
from core.install import DAUFakeInstaller
import locale

class ApplicationOrchestrator:
    """
    Orchestriert den Start der Anwendung.
    Verantwortlich für die Initialisierung des Tkinter-Hauptfensters,
    das Ausführen des Fake-Installers und das Starten der Hauptanwendung.
    """
    def __init__(self, lang):
        """Initialisiert den ApplicationOrchestrator und das Tkinter-Hauptfenster."""
        self.root = tk.Tk()
        # Das Hauptfenster initial absenken, wie im ursprünglichen Skript.
        # DAUApp wird es später mit deiconify() wieder sichtbar machen.
        self.root.withdraw()
        self.root.lower()
        self.main_app = None
        self.lang = lang



    def _launch_main_app(self):
        """Wird als Callback nach dem Installer aufgerufen, um die Hauptanwendung zu starten."""
        self.main_app = DAUApp(self.root)


    def run(self):
        """Startet den Fake-Installer und anschließend die Hauptanwendung."""
        fake_installer = DAUFakeInstaller(self.root, self.lang)
        # Die Methode zum Starten der Haupt-App als Callback übergeben
        fake_installer.start_installation(on_complete_callback=self._launch_main_app)
        
        self.root.mainloop()

if __name__ == "__main__":
    lang = locale.getlocale()[0]
    lang = lang.split("_")[0]

    orchestrator = ApplicationOrchestrator(lang)
    orchestrator.run()
