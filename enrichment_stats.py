import json

with open(
    "enriched_developers.json",
    encoding="utf-8"
) as f:
    developers = json.load(f)

emails = 0
linkedin = 0
github = 0

for dev in developers:

    if dev.get("emails"):
        emails += 1

    if dev.get("linkedin_links"):
        linkedin += 1

    if dev.get("github_links"):
        github += 1

print("Emails:", emails)
print("LinkedIn:", linkedin)
print("GitHub:", github)