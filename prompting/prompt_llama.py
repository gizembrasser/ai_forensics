import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
from prompting.load_models import load_models

# Load environment variables
load_dotenv(find_dotenv())

# Set OpenAI API key
llama_api_key = os.getenv('LLAMA_API_KEY')

client = OpenAI(
api_key = llama_api_key,
base_url = "https://api.llama-api.com"
)

models_file = os.path.join(os.path.dirname(__file__), '../input/llama_models.txt')
models = load_models(models_file)


def get_llama_responses(prompts):
    all_responses = []

    for prompt in prompts:
        response = client.chat.completions.create(
        model="llama-13b-chat",
        messages=[
            {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1024   
        )

        all_responses.append((prompt, response.choices[0].message.content, "llama-13b-chat"))

    return all_responses
        


            