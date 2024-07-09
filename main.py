import os
import csv
from langchain_openai import OpenAI
from langchain_google_genai import GoogleGenerativeAI

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai_api_key = os.getenv('OPENAI_API_KEY')
google_api_key = os.getenv('GOOGLE_API_KEY')
# llama_api_key = os.getenv('LLAMA_API_KEY')

# Configure LangChain
openai_llm = OpenAI(api_key=openai_api_key, max_tokens=1024)
google_llm = GoogleGenerativeAI(
    model="gemini-pro",
    max_output_tokens=1024,
    google_api_key=google_api_key,
)
# llama_llm = HuggingFace(api_key=llama_api_key)


def test_llms(llms, prompt):
    responses = []
    for name, llm in llms.items():
        try:
            response = llm(prompt)
            responses.append((prompt, response, name))
        except Exception as e:
            responses.append((prompt, f"Error: {e}", name))
    return responses

# Define the LLMs to test
llms = {
    'OpenAI': openai_llm,
    # 'Google': google_llm,
    # 'Llama': llama_llm,
}

# Define a prompt
prompt = "What is the capital of France?"

# Test the LLMs
responses = test_llms(llms, prompt)

# Print the responses and write to CSV
csv_file = 'output/responses.csv'

with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['prompt', 'answer', 'model'])
    for response in responses:
        writer.writerow(response)

print(f"Responses have been written to {csv_file}")