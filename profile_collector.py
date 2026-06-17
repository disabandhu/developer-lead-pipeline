import requests
import json
import time

developers = []

with open("usernames.txt", encoding="utf-8") as f:
    usernames = [line.strip() for line in f]

print(f"Found {len(usernames)} usernames")

for username in usernames:

    print(f"Fetching: {username}")

    url = f"https://dev.to/api/users/by_username?url={username}"

    try:

        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            continue

        user = response.json()

        developer = {
            "name": user.get("name"),
            "username": user.get("username"),
            "summary": user.get("summary"),
            "location": user.get("location"),
            "website": user.get("website_url"),
            "twitter": user.get("twitter_username"),
            "github": user.get("github_username"),
            "joined_at": user.get("joined_at")
        }

        developers.append(developer)

        time.sleep(0.5)

    except Exception as e:
        print(e)

with open("developers.json", "w", encoding="utf-8") as f:
    json.dump(developers, f, indent=2, ensure_ascii=False)

print(f"Saved {len(developers)} developers")