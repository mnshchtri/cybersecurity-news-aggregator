from flask import Flask, render_template
from utils.feed_parser import fetch_cybersecurity_feeds
from utils.ai_tools import generate_summary
import spacy

app = Flask(__name__)

# Load NLP model for entity recognition
nlp = spacy.load("en_core_web_sm")

@app.route('/')
def home():
    entries = fetch_cybersecurity_feeds()
    
    # Add NLP processing and summaries
    for entry in entries:
        # Extract entities using spaCy
        doc = nlp(entry['title'] + " " + entry.get('description', ''))
        entry['entities'] = [ent.text for ent in doc.ents if ent.label_ in ['ORG', 'PRODUCT', 'CVE']]
        
        # Generate AI summary
        entry['summary'] = generate_summary(entry.get('description', ''))
    
    return render_template('index.html', entries=entries)

if __name__ == '__main__':
    app.run(debug=True, port=5000)