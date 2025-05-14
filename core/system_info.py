"""
Hilfsfunktionen zum Sammeln und Anzeigen von Systeminformationen,
insbesondere zum Betriebssystem.
"""
import platform
import os

def get_os_details():
    """ Gibt den OS-Namen und ggf. die Linux-Distribution zurück. """
    os_name = platform.system()
    distro_name = None
    if os_name == "Linux":
        distro_name = "Unbekannt"
        try:
            if os.path.exists("/etc/os-release"):
                with open("/etc/os-release") as f:
                    for line in f:
                        if line.startswith("PRETTY_NAME="):
                            distro_name = line.strip().split("=")[1].strip('"')
                            break
        except Exception:
            distro_name = "Linux – aber Distro ist schüchtern"
    return os_name, distro_name

def get_platform_display_text():
    """ Erstellt den Text für das Plattform-Label. """
    os_name, distro = get_os_details()
    label = f"💻 Plattform: {os_name}"
    if os_name == "Linux" and distro:
        label += f" ({distro})"
    elif os_name == "Darwin":
        label += " (macOS – Designerfehler inklusive)"
    elif os_name == "Windows":
        label += " (Windows – Vor Benutzung erst updaten)"
    else:
        label += " (Unbekanntes OS – jetzt wird's wild)"
    return label + " – Möge der Kernel mit dir sein."