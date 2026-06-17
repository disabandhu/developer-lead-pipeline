import requests

usernames = set()

for page in range(1, 11):

    print(f"Page {page}")

    url = f"https://dev.to/api/articles?page={page}&per_page=100"

    articles = requests.get(url).json()

    for article in articles:

        user = article.get("user")

        if user:
            usernames.add(user["username"])

print(f"Found {len(usernames)} usernames")

# SAVE TO FILE
with open("usernames.txt", "w", encoding="utf-8") as f:

    for username in usernames:
        f.write(username + "\n")

print("Saved usernames to usernames.txt")