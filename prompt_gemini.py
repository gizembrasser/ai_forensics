import os
import requests
from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv(find_dotenv())

# Set OpenAI API key
google_api_key = os.getenv('GOOGLE_API_KEY')

def get_gemini_response(prompt):
    headers = {
        "Authorization": f"Bearer {google_api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gemini-pro",  # Adjust as needed
        "prompt": prompt,
        "max_output_tokens": 1024
    }
    response = requests.post("https://api.generativeai.google.com/v1/text", headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["text"].strip()