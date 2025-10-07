import os
import requests
import json
from dotenv import load_dotenv

# Load API key (we'll use this later for game data API)
load_dotenv('backend/config/.env')
api_key = os.environ.get('RIOT_API_KEY')

# Riot esports API endpoint
base = f"https://na1.api.riotgames.com"
endpoint = f"/lol/summoner/v4/summoners/by-puuid/H-f86gQ5FG0zkZ0QtmSYxbx4Qb7H1Lh8i1lQal676nmGWQWf9IlnJ-wFa1dTLONVK5dh1zyyZ7BSew?api_key=RGAPI-9169f75c-e103-4990-9cbc-abe48d48206a"
url = base + endpoint

print("Making API request to Riot Games...")
print(f"URL: {url[:75]}...")

# Riot esports API requires these specific headers
headers = {
    'X-Riot-Key': 'RGAPI-8fa3d442-c328-41e3-875d-469d006acef7'
}

# Make the request with headers
response = requests.get(url)

print(f"\nResponse status code: {response.status_code}")

if response.status_code == 200:
    print("✓ API request successful!")
    data = response.json()
    with open('backend/test.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, sort_keys=True)
    print("Response data saved to 'backend/test.json'")
else:
    print("✗ API request failed")
    print(f"Error: {response.text}")