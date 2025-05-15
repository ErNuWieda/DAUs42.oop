"""
Hilfsfunktionen zum Sammeln und Anzeigen von Systeminformationen,
insbesondere zum Betriebssystem.
"""
import platform
import os
import locale

def get_os_details():
    """ Gibt den OS-Namen und ggf. die Linux-Distribution zurück. """
    os_name = platform.system()
    lang = locale.getlocale()[0]
    lang = lang.split("_")[0]
    distro_name = None
    if os_name == "Linux":
        if lang == "de":
            distro_name = "unbekannt"
        elif lang == "en":
            distro_name = "unknown"
        else:
            print(f"Language {current_locale} not supported, using English instead.")
            lang = "en"
            distro_name = "unknown"            
        try:
            if os.path.exists("/etc/os-release"):
                with open("/etc/os-release") as f:
                    for line in f:
                        if line.startswith("PRETTY_NAME="):
                            distro_name = line.strip().split("=")[1].strip('"')
                            break
        except Exception:
            if lang == "de":
                distro_name = "Linux – aber Distro ist schüchtern"
            else:
                distro_name = "Linux – but distro is shy"            
    
    return os_name, distro_name, lang

def get_platform_display_text():
    """ Erstellt den Text für das Plattform-Label. """
    os_name, distro, lang = get_os_details()
    if lang == "de":
        label = f"💻 Plattform: {os_name}"
    else:
        label = f"💻 Platform: {os_name}"
    if os_name == "Linux" and distro:
        label += f" ({distro})"
    elif os_name == "Darwin":
        if lang == "de":
            label += " (macOS – Designerfehler inklusive)"
        else:
            label += " (macOS – Design flaws included)"
    elif os_name == "Windows":
        if lang == "de":
            label += " (Windows – Vor Benutzung erst updaten)"
        else:
            label += " (Windows – Before using, update"
    else:
        if lang == "de":
            label += " (Unbekanntes OS – jetzt wird's wild)"
        else:
            label += " (Unknown OS – now things are getting wild)"
    if lang == "de":
        label += " – Möge der Kernel mit dir sein."
    else:
        label += " - May the kernel be with you."
    
    return label
