import requests
import os
from dotenv import load_dotenv

load_dotenv()

#gets API key taken from the website from .env

api_key = os.getenv("news_api_key")
url = f"https://newsapi.org/v2/everything?q=tesla&from=2026-08-16&sortBy=publishedAt&apiKey={api_key}"

request = requests.get(url)
content = request.text
print(content)