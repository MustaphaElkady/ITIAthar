# Lab 1: Google Books API

A Python program that searches for books and displays their titles, authors, and publishers. It reads JSON data from Google Books API and stores the results in a `Book` class.

## Setup

Run these commands from the project folder, one at a time:

```powershell
cd week01
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```

Create an API key in Google Cloud Console and enable the Books API. Add your key to `.env`:

```dotenv
GOOGLE_BOOKS_API_KEY=your_api_key_here
```

## Run

```powershell
python main.py
```

Enter a book title or author. The program displays up to five results.

## Keep your key private

Do not upload `.env` or `.venv` to GitHub. Keep them in `.gitignore` and share only `.env.example` without a real key.
