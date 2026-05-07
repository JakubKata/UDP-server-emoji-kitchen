# EmojiKitchen

EmojiKitchen is a lightweight desktop app written in Python for browsing and previewing Google Emoji Kitchen combinations. It uses a simple `PySide6` GUI, loads compatible emoji sets dynamically, and fetches the generated combination image from the remote API.

Examples of supported scenarios:

- Selecting the first emoji and seeing compatible options for the second one
- Selecting the second emoji and seeing compatible options for the first one
- Previewing the resulting Emoji Kitchen image directly in the app
- Using a local `.env` file to keep the API key out of version control

---

## Features

- Desktop GUI built with `PySide6`
- Dynamic emoji selection lists
- Emoji combination lookup through the API layer in `api/`
- Image preview rendered directly in the main window
- Environment-based configuration with `python-dotenv`
- Clear separation between UI code and API logic

---

## Requirements

- Python 3.8 or newer
- Virtual environment recommended
- `PySide6`
- `requests`
- `python-dotenv`
- `protobuf`
- Internet access for fetching emoji data and images
- A valid `API_KEY` for the remote Emoji Kitchen / Tenor endpoint

The project is licensed under the MIT License (see `LICENSE`).

---

## Quick Start (Windows / Linux)

1. Create and activate a virtual environment:

```bash
python -m venv .venv
# Linux / macOS
source .venv/bin/activate
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a local `.env` file from the example and set your API key:

```bash
copy .env.example .env
```

Update the `API_KEY` value in `.env` before running the app.

---

## Run

Start the application:

```bash
python main.py
```

The main window lets you choose two emojis and shows the resulting combination image when one is available.

---

## Usage (brief)

1. Open the app.
2. Click the first or second emoji field to pick an emoji from the available list.
3. After both emojis are selected, the app queries the API and previews the generated image.

---

## Project Structure

```text
EmojiKitchen/
├── LICENSE
├── README.md
├── main.py
├── requirements.txt
├── .env.example
├── api/
│   ├── emoji_combination_api.py
│   ├── emoji_kitchen_api.py
│   └── network.py
├── proto/
│   └── schema_pb2.py
└── ui/
    ├── ui_EmojiKitchen.py
    └── ui_EmojiList.py
```

---

## License

MIT