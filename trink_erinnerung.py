from plyer import notification
import random
import os
import sys
import threading
import time
from PIL import Image
import pystray
from pystray import MenuItem as item, Menu

# Definiere eine Liste mit verschiedenen Erinnerungsnachrichten 
toasts = [
    "Trinken oder welken - du entscheidest!",
    "Deine Pflanzen wollen, dass du auch mal trinkst!",
    "Mehr Wasser, weniger Sorgen!",
    "Hydriert bleiben, sonst wirst du zum Trockenobst!",
    "Hey, dein Körper freut sich über einen Schluck Wasser!",
    "Dein Gehirn liebt Wasser - tu ihm den Gefallen!",
    "Ein Glas Wasser und die Welt sieht gleich besser aus!",
    "Hydriert = motiviert! Los, trink einen Schluck!",
    "Power up! Dein Körper braucht Flüssigkeit!",
    "Ohne Wasser keine Energie - schnapp dir dein Glas!",
    "Dein Körper ist eine Maschine - gib ihm den richtigen Treibstoff!",
    "Dein Körper besteht zu 70% aus Wasser - Zeit, den Vorrat aufzufüllen!",
    "Dein Gehirn ruft an: Es will mehr Wasser!",
    "Bleib hydratisiert - du bist schließlich kein Kaktus!",
    "Trink Wasser - sonst quietscht dein Gehirn beim Denken!",
    "Mehr Wasser, weniger Falten. Ich sag´s ja nur…",
    "Wasser ist quasi flüssige Produktivität. Gönn dir!",
    "Hydration ist wie ein Schutzschild gegen miese Laune!",
    "Deine Nieren haben mir geschrieben: Sie wollen mehr Wasser!"]

# Helferfunktion für Pfade in PyInstaller
def resource_path(relative_path):
    """Pfad für Icon im Build mit PyInstaller"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Trink-Erinnerung  
def drink_notification():
    """Trink-Erinnerung als Desktop-Benachrichtigung anzeigen"""
    notification.notify(
        title="Trink-Erinnerung",
        message=random.choice(toasts),
        app_name="Trink-Erinnerung",
        app_icon=resource_path("icon.ico"),
        timeout=30
    )

# Schleife für regelmäßige Erinnerungen
INTERVAL = 30 * 60  # 30 Minuten, anpassbar

def notification_loop():
    while True:
        drink_notification()
        time.sleep(INTERVAL)

# Tray-Icon und Menü
def quit_action(icon, item):
    icon.stop()

def start_tray():
    # Icon laden
    icon_image = Image.open(resource_path("icon.ico"))
    # Menü für Tray
    menu = Menu(item("Beenden", quit_action))
    # Tray-Icon erstellen
    icon = pystray.Icon("Trink-Erinnerung", icon_image, "Trink-Erinnerung", menu)
    # Benachrichtigungen in eigenem Thread starten
    threading.Thread(target=notification_loop, daemon=True).start()
    # Tray starten
    icon.run()

# Hauptprogramm
if __name__ == "__main__":
    start_tray()