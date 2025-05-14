"""
Hilfsfunktionen für die Benutzeroberfläche (UI) der DAUs42-Anwendung,
insbesondere für die Erstellung und Verwaltung von Tooltips.
"""
import tkinter as tk

def show_tooltip(widget, text):
    """ Zeigt ein Tooltip-Fenster an. """
    tooltip = tk.Toplevel(widget)
    tooltip.wm_overrideredirect(True) # Fenster ohne Standard-Dekorationen
    tooltip.geometry(f"+{widget.winfo_rootx()+30}+{widget.winfo_rooty()+20}")
    label = tk.Label(tooltip, text=text, background="#ffffe0", relief="solid", borderwidth=1)
    label.pack()
    return tooltip

def add_tooltip(widget, text):
    """ Fügt einem Widget ein Tooltip hinzu, das bei Mouse-Enter/-Leave erscheint/verschwindet. """
    tooltip_window = None

    def on_enter(event):
        nonlocal tooltip_window
        # Verhindert das Erstellen mehrerer Tooltips, falls das Event schnell hintereinander ausgelöst wird
        if tooltip_window is None:
            tooltip_window = show_tooltip(widget, text)

    def on_leave(event):
        nonlocal tooltip_window
        if tooltip_window:
            tooltip_window.destroy()
            tooltip_window = None # Wichtig, um den Zustand zurückzusetzen

    widget.bind("<Enter>", on_enter)
    widget.bind("<Leave>", on_leave)