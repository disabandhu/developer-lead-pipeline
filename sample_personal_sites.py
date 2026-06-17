import json
from website_classifier import classify_website

with open("developers.json", encoding="utf-8") as f:
    developers = json.load(f)

count = 0

for dev in developers:

    website = dev.get("website")

    if classify_website(website) == "personal":

        print(website)

        count += 1

        if count == 20:
            break