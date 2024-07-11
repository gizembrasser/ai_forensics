import os
import openai
from dotenv import load_dotenv, find_dotenv
from prompting.load_models import load_models

# Load environment variables
load_dotenv(find_dotenv())

# Set OpenAI API key
openai_api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = openai_api_key

# Path to the models file
models_file = os.path.join(os.path.dirname(__file__), '../input/models/gpt_models.txt')
models = load_models(models_file)


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
