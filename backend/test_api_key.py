import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv('backend/config/.env')

# Try to get the API key
api_key = os.environ.get('RIOT_API_KEY')

if api_key:
    print("✓ API Key loaded successfully!")
    print(f"Key starts with: {api_key[:10]}...")  # Show first 10 characters only
else:
    print("✗ API Key NOT found")
    print("Make sure you created the .env file with your key")