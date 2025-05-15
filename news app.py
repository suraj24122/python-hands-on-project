# import requests

# query = input("Search News = ")
# api = "d80fbeb0e928471ea938e1816971c5d1"

# url = f"https://newsapi.org/v2/everything?q={query}&from=2025-04-15&sortBy=publishedAt&apiKey={api}"
# print(url)

# r = requests.get(url)

# data = r.json()
# articles = data["articles"]

# for index, article in enumerate(articles):
#     print(index + 1 ,article["title"], article["url"])
#     print("*****************************************\n")
