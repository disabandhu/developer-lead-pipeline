import json

with open(
    "enriched_developers.json",
    encoding="utf-8"
) as f:
    developers = json.load(f)

for dev in developers:

    score = 0

    if dev.get("emails"):
        score += 5

    if dev.get("linkedin_links"):
        score += 3

    if dev.get("github_links"):
        score += 3

    if dev.get("website"):
        score += 2

    if dev.get("summary"):
        score += 1

    dev["lead_score"] = score

developers.sort(
    key=lambda x: x["lead_score"],
    reverse=True
)

with open(
    "ranked_developers.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        developers,
        f,
        indent=2,
        ensure_ascii=False
    )

print("Done")