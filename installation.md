# CSV Analyzer Extended

Ein leistungsstarkes Tool für die Analyse und Filterung von CSV-Dateien mit erweiterten Funktionen für Clustering, Kreuzvalidierung, Export in verschiedene Formate und vieles mehr.

## Installation

### Schritt 1: Virtuelle Umgebung erstellen

Es wird empfohlen, eine virtuelle Umgebung zu verwenden, um Abhängigkeiten zu isolieren. Um eine virtuelle Umgebung zu erstellen, führe folgende Schritte aus:

1. Öffne ein Terminal oder eine Eingabeaufforderung.
2. Navigiere zu dem Verzeichnis, in dem du das Projekt installieren möchtest.
3. Erstelle eine neue virtuelle Umgebung:

   ```bash
   python3 -m venv venv
   ```

4. Aktiviere die virtuelle Umgebung:

   - Auf **Windows**:

     ```bash
     venv\Scripts\activate
     ```

   - Auf **macOS** und **Linux**:

     ```bash
     source venv/bin/activate
     ```

5. Überprüfe, ob die virtuelle Umgebung aktiv ist (dein Terminal sollte nun `venv` oder einen ähnlichen Namen anzeigen).

### Schritt 2: Abhängigkeiten installieren

Du hast zwei Optionen, um die benötigten Bibliotheken zu installieren: entweder mit der `requirements.txt` oder mit der `setup.py`.

#### Option 1: Installation mit `requirements.txt`

1. Stelle sicher, dass du dich in der virtuellen Umgebung befindest.
2. Führe den folgenden Befehl aus, um alle Abhängigkeiten aus der `requirements.txt` zu installieren:

   ```bash
   pip install -r requirements.txt
   ```

Dies installiert alle benötigten Bibliotheken für das Projekt.

#### Option 2: Installation mit `setup.py`

1. Stelle sicher, dass du dich in der virtuellen Umgebung befindest.
2. Führe den folgenden Befehl aus, um das Projekt und alle Abhängigkeiten über die `setup.py` zu installieren:

   ```bash
   pip install .
   ```

Dies wird sowohl das Projekt als auch die benötigten Abhängigkeiten installieren.

### Schritt 3: Verwendung des Projekts

Nach der Installation kannst du das Projekt verwenden, indem du die entsprechenden Skripte oder Module ausführst. Stelle sicher, dass du immer die virtuelle Umgebung aktiviert hast, bevor du das Projekt startest.

### Deaktivierung der virtuellen Umgebung

Wenn du die virtuelle Umgebung beenden möchtest, kannst du den folgenden Befehl ausführen:

```bash
deactivate
```

Dies wird die virtuelle Umgebung deaktivieren und dich zurück zu deinem regulären Python-Interpreter bringen.

## Weitere Informationen

- Stelle sicher, dass alle notwendigen Bibliotheken in der virtuellen Umgebung installiert sind, bevor du das Projekt verwendest.
- Für spezifische Informationen zu den Funktionen des Projekts, sieh dir die Dokumentation der einzelnen Module an.


### Was wird abgedeckt:
1. Erstellung einer virtuellen Umgebung mit `venv`.
2. Aktivierung der virtuellen Umgebung für **Windows**, **macOS**, und **Linux**.
3. Installation der Abhängigkeiten entweder mit `requirements.txt` oder mit `setup.py`.
4. Deaktivierung der virtuellen Umgebung nach der Arbeit.

