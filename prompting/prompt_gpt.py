import os
import openai
from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv(find_dotenv())

# Set OpenAI API key
openai_api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = openai_api_key

models = [
    "gpt-4", "gpt-4o", "gpt-4-turbo", "gpt-4-0125-preview", 
    "gpt-4-1106-preview", "gpt-4-0613", 
    "gpt-3.5-turbo-0125", "gpt-3.5-turbo-1106"
]

def get_gpt_responses(prompts):
    all_responses = []
    
    for prompt in prompts:
        for model in models:
            response = openai.ChatCompletion.create(
                model=model,  # Specify the model
                messages=[{"role": "user", "content": prompt}],
                max_tokens=1024,
                temperature=0.7
            )
            all_responses.append((prompt, response.choices[0].message["content"].strip(), model))
    
    return all_responses
