import requests
import os

API_TOKEN = os.getenv("COC_API_TOKEN")

BASE_URL = "https://api.clashofclans.com/v1"


headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

def get_clan_details(clan_tag):

    encoded_tag = clan_tag.replace(
        "#",
        "%23"
    )

    url = f"{BASE_URL}/clans/{encoded_tag}"

    response = requests.get(
        url,
        headers=headers
    )

    return response.json()

def get_clan_members(clan_tag):

    encoded_tag = clan_tag.replace("#", "%23")

    url = f"{BASE_URL}/clans/{encoded_tag}/members"

    response = requests.get(url, headers=headers)

    return response.json()

def get_current_war(clan_tag):

    encoded_tag = clan_tag.replace("#", "%23")

    url = f"{BASE_URL}/clans/{encoded_tag}/currentwar"

    response = requests.get(url, headers=headers)

    return response.json()

