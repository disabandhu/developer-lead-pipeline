from dev_api import get_user
from website_parser import extract_website_data

user = get_user("shubhradev")

website = user.get("website_url")

data = extract_website_data(website)

print(data)