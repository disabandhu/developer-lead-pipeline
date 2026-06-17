import json
from website_classifier import classify_website

counts = {}

with open("developers.json", encoding="utf-8") as f:
    developers = json.load(f)

for dev in developers:

    website = dev.get("website")

    website_type = classify_website(website)

    counts[website_type] = counts.get(website_type, 0) + 1

print(counts)