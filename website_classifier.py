from urllib.parse import urlparse

def classify_website(url):

    if not url:
        return "none"

    domain = urlparse(url).netloc.lower()

    if "linkedin.com" in domain:
        return "linkedin"

    if "github.com" in domain:
        return "github"

    if "medium.com" in domain:
        return "medium"

    if "substack.com" in domain:
        return "substack"

    return "personal"