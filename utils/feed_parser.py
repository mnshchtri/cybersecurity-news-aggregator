import feedparser
import json
import os
from datetime import datetime

def fetch_cybersecurity_feeds():
    feeds_path = os.path.join(os.path.dirname(__file__), '../feeds/sources.json')
    with open(feeds_path) as f:
        sources = json.load(f)
    
    entries = []
    
    for source in sources['feeds']:
        feed = feedparser.parse(source['url'])
        for entry in feed.entries:
            entries.append({
                'title': entry.title,
                'link': entry.link,
                'published': datetime(*entry.published_parsed[:6]),
                'source': source['name'],
                'description': entry.get('description', ''),
                'category': source['category']
            })
    
    # Sort by publication date
    entries.sort(key=lambda x: x['published'], reverse=True)
    
    return entries[:50]  # Return latest 50 entries