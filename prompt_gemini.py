import os
from dotenv import load_dotenv, find_dotenv
from langchain_google_genai import GoogleGenerativeAI

# Load environment variables
load_dotenv(find_dotenv())

# Set OpenAI API key
gemini_api_key = os.getenv('GOOGLE_API_KEY')

models = [
    "gemini-pro", "gemini-1.5-pro", 
    "gemini-1.5-flash", "gemini-1.0-pro", 
]

def get_gemini_response(prompt):
    responses = []

    for model in models:
        gemini_llm = GoogleGenerativeAI(
            model=model, # Specify the model
            max_output_tokens=1024,
            google_api_key=gemini_api_key,
        )

        response = gemini_llm(prompt)
        responses.append((prompt, response, model))
    
    return responses
