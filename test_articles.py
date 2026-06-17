import requests

url = "https://dev.to/api/articles?page=1&per_page=10"

response = requests.get(url)

print(response.json()[0])