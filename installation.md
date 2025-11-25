# Anleitung zur Installation von Python mit Anaconda und VS Code

## Schritt 1: Anaconda herunterladen und installieren

1. **Anaconda herunterladen**
   - Besuche die [Anaconda-Website](https://www.anaconda.com/products/distribution).
   - Klicke auf "Download" und wähle die Version für dein Betriebssystem (Windows, macOS oder Linux).
   - Lade das Installationsprogramm herunter.

2. **Anaconda installieren**
   - Führe das heruntergeladene Installationsprogramm aus.
   - Folge den Anweisungen des Installationsassistenten. Die Standardoptionen sind in der Regel ausreichend.
   - Stelle sicher, dass du die Option auswählst, Anaconda zu deinem PATH hinzuzufügen (dies ist besonders wichtig auf Windows).

## Schritt 2: Visual Studio Code herunterladen und installieren

1. **Visual Studio Code herunterladen**
   - Besuche die [VS Code-Website](https://code.visualstudio.com/).
   - Klicke auf "Download" und wähle die Version für dein Betriebssystem.

2. **Visual Studio Code installieren**
   - Führe das heruntergeladene Installationsprogramm aus.
   - Folge den Anweisungen des Installationsassistenten.
   - Aktiviere die Option "Add to PATH" (wichtig für die Verwendung des `code`-Befehls im Terminal).

## Schritt 3: Python-Umgebung in Anaconda erstellen

1. **Anaconda Navigator öffnen**
   - Öffne den Anaconda Navigator über das Startmenü (Windows) oder den Anwendungen-Ordner (macOS).

2. **Neue Umgebung erstellen**
   - Klicke auf "Environments" im linken Menü.
   - Klicke auf "Create" und gib einen Namen für die neue Umgebung ein.
   - Wähle die Python-Version aus, die du verwenden möchtest (z.B. Python 3.8).
   - Klicke auf "Create" und warte, bis die Umgebung erstellt ist.

## Schritt 4: Anaconda-Umgebung in VS Code integrieren

1. **Visual Studio Code öffnen**
   - Starte VS Code.

2. **Python-Extension installieren**
   - Klicke auf das Extensions-Symbol in der linken Seitenleiste (oder drücke `Ctrl+Shift+X`).
   - Suche nach "Python" und installiere die von Microsoft entwickelte Python-Extension.

3. **Python-Interpreter auswählen**
   - Öffne die Kommando-Palette (`Ctrl+Shift+P` oder `Cmd+Shift+P` auf macOS).
   - Tippe "Python: Select Interpreter" und wähle die gewünschte Anaconda-Umgebung aus der Liste aus.

## Schritt 5: Erste Python-Datei erstellen und ausführen

1. **Neue Datei erstellen**
   - Klicke auf "File" > "New File" oder drücke `Ctrl+N`.
   - Speichere die Datei mit der Endung `.py` (z.B. `hello_world.py`).

2. **Python-Code schreiben**
   - Füge folgenden Code in die Datei ein:
     ```python
     print("Hello, World!")
     ```

3. **Python-Datei ausführen**
   - Öffne ein Terminal in VS Code (`Ctrl+` oder `Cmd+` auf macOS).
   - Stelle sicher, dass die Anaconda-Umgebung aktiviert ist:
     ```bash
     conda activate <name-der-umgebung>
     ```
   - Führe die Python-Datei aus:
     ```bash
     python hello_world.py
     ```

## Fertig!
Du hast jetzt erfolgreich Python mit Anaconda und VS Code installiert und konfiguriert. Viel Spaß beim Programmieren!
