import requests
import json

def fetchRandomUser():
    url="https://api.freeapi.app/api/v1/public/randomusers"
    response = requests.get(url).json()
    return response["data"]["data"]["gender"]
print(fetchRandomUser())