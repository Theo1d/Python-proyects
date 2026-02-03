import requests

endpoint = "https://www.googleapis.com/books/v1/volumes"
query = "moby dick"

params = {"q": query, "maxResults": 3}
response = requests.get(endpoint, params=params).json()
for book in response["items"]:
    volume = book["volumeInfo"]
    title = volume.get("title", "")
    published = volume.get("publishedDate", "")
    description = volume.get("description", "")
    print(f"{title} ({published})\n{description}\n")
