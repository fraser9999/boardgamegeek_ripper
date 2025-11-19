

### `README.md`

````markdown
# Board Game Geek - Game Info Downloader / Ripper

**Author:** Hermann Knopp  
**Contact:** hermann.knopp@gmx.at  
**Version:** 0.1alpha (early alpha version)

---

## Übersicht

Dieses Python-Skript lädt Beschreibungen und Informationen von Brettspielen von [BoardGameGeek](https://boardgamegeek.com) und speichert sie als formatierte Textdateien. Die Daten eignen sich besonders zur Weiterverarbeitung oder zum Training von GPT-2 Chatbot-Datensätzen.

Das Skript kann die Datenerstellung jederzeit unterbrechen und an einer beliebigen Brettspiel-ID fortsetzen.

---

## Funktionen

- Lädt Spielinformationen wie:
  - Name, Beschreibung, Typ
  - Spieleranzahl (min/max)
  - Spieldauer (min/max/average)
  - Mindestalter
  - Erscheinungsjahr
  - Publisher (optional, kann bei Sonderzeichen Probleme verursachen)
- Speichert alle Daten als Textdateien in einem eigenen Ordner `gamestories`.
- Pause von 2–3 Sekunden zwischen Downloads, um den BGG-Server nicht zu überlasten.
- Fehler- und Sonderzeichen-handling:
  - Das Skript ist relativ robust gegen Sonderzeichen.
  - Im Fehlerfall kann die Datenerstellung an der letzten Spiel-ID fortgesetzt werden.

---

## Voraussetzungen

- Python 3.10.x  
- Bibliotheken:
  - `libbgg` (Version 2 API)
  - `textwrap` (Standardbibliothek)
  - `json` (Standardbibliothek)

Empfohlene Installation der benötigten Bibliotheken:

```bash
pip install -r requirements.txt
````

---

## Installation

1. Repository klonen:

```bash
git clone <repository-url>
cd <repository-folder>
```

2. Virtuelle Umgebung erstellen (optional):

```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
```

3. Abhängigkeiten installieren:

```bash
pip install -r requirements.txt
```

---

## Nutzung

1. Skript starten:

```bash
python bgg-ripper3.py
```

2. Eingabe der Start-ID (optional):

* Drücke `Enter` für ID = 1.
* Oder gib eine spezifische Brettspiel-ID ein, um das Herunterladen fortzusetzen.

3. Die Spielinformationen werden im Ordner `gamestories` als Textdateien gespeichert.

---

## Hinweise

* Bei mehreren tausend Downloads ist Geduld erforderlich, da das Skript bewusst Pausen zwischen den Anfragen einlegt.
* Bei "Too Many Requests"-Fehlern wartet das Skript automatisch 15 Sekunden und versucht es erneut.
* Sonderzeichen in den Spieletiteln werden für Dateinamen automatisch bereinigt.

---

## Dateistruktur

* `bgg-ripper.py` – ursprüngliches Skript, unformatierte Textausgabe.
* `bgg-ripper2.py` – formatierte Textausgabe, stabiler als `bgg-ripper.py`.
* `bgg-ripper3.py` – verbesserte Version mit Fehlerbehandlung, Statusmeldungen und formatierter Textausgabe.

---

## Lizenz

Nur für private oder Forschungszwecke. Die Nutzung muss die Nutzungsbedingungen von BoardGameGeek beachten.

```

---

### `requirements.txt`

```

libbgg>=2.0.0

```

> Hinweis: `textwrap` und `json` sind Standardbibliotheken von Python 3.10, müssen also nicht installiert werden.

