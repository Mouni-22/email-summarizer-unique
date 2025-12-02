from flask import Flask, request, jsonify, send_from_directory
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
import os

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/api/summarize', methods=['POST'])
def summarize():
    data = request.get_json() or {}
    text = data.get('text', '')
    sentences_count = int(data.get('sentences', 3))
    if not text.strip():
        return jsonify({'error': 'No text provided.'}), 400
    parser = PlaintextParser.from_string(text, Tokenizer('english'))
    summarizer = LexRankSummarizer()
    sentences = summarizer(parser.document, sentences_count)
    summary = ' '.join(str(s) for s in sentences)
    return jsonify({'summary': summary})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
