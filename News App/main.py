import requests 

query = input("what type of news are you looking for?")
api = "e4307520a75b4ddf85a817ca1b285aa0"
url = f"https://newsapi.org/v2/everything?q={query}&from=2025-06-10&sortBy=publishedAt&apiKey=e4307520a75b4ddf85a817ca1b285aa0"

print(url)
r = requests.get(url)

data = r.json()
articles = data["articles"]

for article in articles:
    print(article["title"], article["url"])
    print("\n**********************************\n")
