import json
import time

from website_enrichment import enrich_website
from website_classifier import classify_website

with open("developers.json", encoding="utf-8") as f:
    developers = json.load(f)

enriched = []

total = len(developers)

for index, dev in enumerate(developers, start=1):

    website = dev.get("website")

    print(f"[{index}/{total}] {website}")

    if website and classify_website(website) == "personal":

        result = enrich_website(website)

        if result:

            dev["emails"] = result["emails"]
            dev["linkedin_links"] = result["linkedin"]
            dev["github_links"] = result["github"]
            dev["twitter_links"] = result["twitter"]

    enriched.append(dev)

    time.sleep(1)

with open(
    "enriched_developers.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        enriched,
        f,
        indent=2,
        ensure_ascii=False
    )

print("Done")