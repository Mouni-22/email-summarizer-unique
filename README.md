# Email Summarizer (unique)

Lightweight Flask starter that summarizes text using an extractive summarizer (LexRank via sumy).

## Quick start (Linux / macOS)
1. Create venv: `python3 -m venv venv && source venv/bin/activate`
2. Install: `pip install -r requirements.txt`
3. Setup NLTK (first run only):
   ```py
   python -c "import nltk; nltk.download('punkt')"
   ```
4. Run: `python app.py`
5. Open `http://localhost:5000` and paste text.

## API
`POST /api/summarize` JSON `{ "text": "...", "sentences": 3 }` → `{ "summary": "..." }`
