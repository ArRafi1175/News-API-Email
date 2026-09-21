import requests
import os
from send_email import send_email

from django.template.defaultfilters import title
from dotenv import load_dotenv

load_dotenv()

#gets API key taken from .env

api_key = os.getenv("news_api_key")
url = f"https://newsapi.org/v2/everything?q=tesla&from=2026-08-21&sortBy=publishedAt&apiKey={api_key}"

# Make request
request = requests.get(url)

# Get a dictionary with Data
content = request.json()

# Access the article titles and descriptions

body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + str(article["title"]) + "\n" + str(article["description"]) + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
