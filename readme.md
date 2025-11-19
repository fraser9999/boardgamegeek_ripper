
### `README.md` 

````markdown
# Board Game Geek - Game Info Downloader / Ripper

**Author:** Hermann Knopp  
**Contact:** hermann.knopp@gmx.at  
**Version:** 0.1alpha (early alpha version)

---

## Overview

This Python script downloads descriptions and information about board games from [BoardGameGeek](https://boardgamegeek.com) and saves them as formatted text files. The data is especially suitable for further processing or training GPT-2 chatbot datasets.

The script can pause data creation at any time and resume from any board game ID.

---

## Features

- Downloads game information such as:
  - Name, description, type
  - Number of players (min/max)
  - Playtime (min/max/average)
  - Minimum age
  - Year published
  - Publisher (optional; may cause issues with special characters)
- Saves all data as text files in a dedicated folder `gamestories`.
- 2–3 seconds pause between downloads to avoid overloading the BGG server.
- Error and special character handling:
  - The script is relatively robust against special characters.
  - If an error occurs, data creation can be resumed from the last game ID.

---

## Requirements

- Python 3.10.x  
- Libraries:
  - `libbgg` (version 2 API)
  - `textwrap` (standard library)
  - `json` (standard library)

Install required libraries:

```bash
pip install -r requirements.txt
````

---

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd <repository-folder>
```

2. (Optional) Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

1. Run the script:

```bash
python bgg-ripper3.py
```

2. Enter the start ID (optional):

* Press `Enter` for ID = 1.
* Or provide a specific board game ID to resume downloading.

3. Game information will be saved as text files in the `gamestories` folder.

---

## Notes

* For several thousand downloads, patience is required because the script intentionally pauses between requests.
* On "Too Many Requests" errors, the script waits 15 seconds and retries automatically.
* Special characters in game titles are automatically sanitized for filenames.

---

## File Structure

* `bgg-ripper.py` – original script, unformatted text output.
* `bgg-ripper2.py` – formatted text output, more stable than `bgg-ripper.py`.
* `bgg-ripper3.py` – improved version with error handling, status messages, and formatted text output.

---

## License

For private or research use only. Usage must comply with BoardGameGeek's terms of service.

```

