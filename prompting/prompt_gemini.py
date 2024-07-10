import os
from dotenv import load_dotenv, find_dotenv
from langchain_google_genai import GoogleGenerativeAI
from prompting.load_models import load_models

# Load environment variables
load_dotenv(find_dotenv())

# Set OpenAI API key
gemini_api_key = os.getenv('GOOGLE_API_KEY')

# Path to the models file
models_file = os.path.join(os.path.dirname(__file__), '../input/gemini_models.txt')
models = load_models(models_file)


def get_gemini_responses(prompts):
    all_responses = []

    for prompt in prompts:
        for model in models:
            gemini_llm = GoogleGenerativeAI(
                model=model, # Specify the model
                max_output_tokens=1024,
                google_api_key=gemini_api_key,
            )

            response = gemini_llm(prompt)
            all_responses.append((prompt, response, model))
    
    return all_responses