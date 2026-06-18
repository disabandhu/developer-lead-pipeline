# Developer Intelligence Pipeline 🚀

A data enrichment pipeline that discovers developer profiles, collects public information, enriches profiles from multiple sources, and generates structured developer datasets.

The goal is to build a developer intelligence dataset containing:

- Developer identity
- Contact information
- Social profiles
- GitHub activity
- Companies
- Roles
- Skills
- Developer quality scoring

---

## Current Status

🚧 **Scaling and enrichment improvements in progress**

Current pipeline is functional and collecting/enriching developer profiles.

### Current Dataset

Processed:

- 632+ developers discovered
- 400+ personal websites analyzed
- 150+ emails extracted
- 190+ LinkedIn profiles found
- 200+ GitHub profiles discovered

---

## Output

The cleaned dataset is exported as:
developers.csv


CSV contains structured developer information:

| Field | Description |
|---|---|
| name | Developer name |
| username | Platform username |
| location | Developer location |
| email | Extracted email |
| website | Personal website |
| linkedin | LinkedIn profile |
| github | GitHub profile |
| company | Company information |
| role | Developer role |
| skills | Extracted technologies |
| followers | GitHub followers |
| repositories | Public repository count |
| lead_score | Developer quality score |

---

## Data Pipeline
DEV API
|
v
Developer Discovery
|
v
Profile Collection
|
v
Website Enrichment
|
v
Email Extraction
|
v
LinkedIn Extraction
|
v
GitHub Extraction
|
v
GitHub API Enrichment
|
v
Company
|
v
Bio
|
v
Followers
|
v
Repository Data
|
v
Skill Extraction
|
v
Lead Scoring
|
v
CSV / JSON Export


---

## Features Completed ✅

### Developer Discovery

- DEV.to API integration
- Username collection
- Profile extraction

Collected:

- Name
- Username
- Summary
- Location
- Website
- Social links

---

### Website Enrichment

Personal websites are analyzed to extract:

- Email addresses
- LinkedIn profiles
- GitHub profiles
- Social links

---

### GitHub Enrichment

GitHub API integration provides:

- GitHub username
- Bio
- Company
- Followers
- Following
- Repository count
- Account creation date

---

### Lead Scoring

Developers are scored based on available information.

Example:
Email +5
LinkedIn +3
GitHub +3
Website +2


Higher scores indicate richer profiles.

---

## Tech Stack

- Python
- Requests
- BeautifulSoup
- DEV API
- GitHub API
- JSON
- CSV

---


---

## Scaling Work 🚧

Currently improving:

- Larger developer discovery
- Tag-based DEV crawling
- More profile sources
- Better skill extraction
- Repository analysis
- Duplicate removal
- Improved ranking

Future sources planned:

- GitHub repositories
- Developer communities
- Startup platforms
- Portfolio websites

---

## Future Improvements

- Repository language analysis
- Technology stack detection
- AI-based skill extraction
- Database storage
- Search dashboard
- Developer similarity matching

---

## Goal

Transform public developer profiles into structured, searchable developer intelligence data.
