import json
from website_enrichment import enrich_website

with open("developers.json", encoding="utf-8") as f:
    developers = json.load(f)

for dev in developers:

    website = "https://eevis.codes"

    if website:

        print("Testing:", website)

        result = enrich_website(website)

        print(result)

        break