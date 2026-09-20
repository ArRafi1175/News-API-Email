import requests
import os
from dotenv import load_dotenv

load_dotenv()

#gets API key taken from .env

api_key = os.getenv("news_api_key")
url = f"https://newsapi.org/v2/everything?q=tesla&from=2026-08-20&sortBy=publishedAt&apiKey={api_key}"

# Make request
request = requests.get(url)

# Get a dictionary with Data
content = request.json()

# Access the article titles and descriptions
for article in content["articles"]:
    print(article["title"])
    print(article["description"])