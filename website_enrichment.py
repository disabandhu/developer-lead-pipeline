import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin

EMAIL_REGEX = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

PAGES = [
    "",
    "/about",
    "/contact",
    "/about-me",
    "/contact-me"
]

def enrich_website(base_url):

    emails = set()

    linkedin = set()
    github = set()
    twitter = set()

    try:

        for page in PAGES:

            url = urljoin(base_url, page)

            try:

                html = requests.get(
                    url,
                    timeout=5,
                    headers={
                        "User-Agent": "Mozilla/5.0"
                    }
                ).text

                emails.update(
                    re.findall(EMAIL_REGEX, html)
                )

                soup = BeautifulSoup(
                    html,
                    "html.parser"
                )

                for a in soup.find_all("a", href=True):

                    href = a["href"]

                    if "linkedin.com" in href:
                        linkedin.add(href)

                    if "github.com" in href:
                        github.add(href)

                    if "twitter.com" in href or "x.com" in href:
                        twitter.add(href)

            except:
                pass

        return {
            "emails": list(emails),
            "linkedin": list(linkedin),
            "github": list(github),
            "twitter": list(twitter)
        }

    except Exception:
        return None