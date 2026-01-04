# Trink-Erinnerung

Die **Trink-Erinnerung** ist eine kleine Desktop-Anwendung für Windows, die dich regelmäßig ans Trinken erinnert. Sie läuft im **Tray**, zeigt motivierende Benachrichtigungen und kann automatisch beim Windows-Start gestartet werden.

## Funktionen
## Funktionen

- Zufällige motivierende Trink-Erinnerungen  
- Tray-Icon mit Rechtsklick-Menü zum Beenden  
- Anpassbare Intervalle zwischen den Erinnerungen  
- Läuft als eigenständige **exe** – kein Python nötig  

## Nutzung

### Exe starten

- Einfach `trink_erinnerung.exe` ausführen  
- Die Anwendung läuft dann im Tray  
- Notifications erscheinen automatisch  

### Tray-Icon-Menü

- Rechtsklick auf das Icon → **Beenden**, um die Anwendung zu schließen  

## Automatischer Start beim Windows-Start

### Option 1: Autostart-Ordner

1. Drücke `Win + R` → `shell:startup` → Enter  
2. Füge eine Verknüpfung zu deiner exe hinzu  

### Option 2: Task Scheduler

1. Task Scheduler öffnen (`Win + S` → „Task Scheduler“)  
2. Neue Aufgabe erstellen → Name vergeben (z. B. „Trink-Erinnerung“)  
3. Trigger → **At log on** auswählen  
4. Aktion → **Start a program** → Pfad zu deiner exe  
5. Fertig → Testen  

## Anpassungen

- Die Nachrichten kannst du im `trink_erinnerung.py`-Code im `toasts`-Array ändern und die exe neu bauen  
- Das Icon der exe kann ebenfalls im Code angepasst werden  

💧 Viel Spaß und bleib hydriert!
