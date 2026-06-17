import json

with open("developers.json", encoding="utf-8") as f:
    developers = json.load(f)

websites = 0

for dev in developers:
    if dev.get("website"):
        websites += 1

print("Total developers:", len(developers))
print("Developers with websites:", websites)