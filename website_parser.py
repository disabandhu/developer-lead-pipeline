import requests
from bs4 import BeautifulSoup
import re

EMAIL_REGEX = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

def extract_website_data(url):

    try:
        html = requests.get(url, timeout=10).text

        emails = re.findall(EMAIL_REGEX, html)

        soup = BeautifulSoup(html, "html.parser")

        links = []

        for a in soup.find_all("a", href=True):
            links.append(a["href"])

        return {
            "emails": list(set(emails)),
            "links": links
        }

    except Exception:
        return None