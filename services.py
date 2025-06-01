import requests

API_URL = "http://universities.hipolabs.com/search"

def fetch_universities_by_country(country: str):
    response = requests.get(API_URL, params={"country": country})
    return response.json()

def fetch_universities_by_name(name: str):
    response = requests.get(API_URL, params={"name": name})
    return response.json()

