import requests

def get_user(username):
    url = f"https://dev.to/api/users/by_username?url={username}"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return None