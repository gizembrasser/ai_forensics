import os
import csv
from prompt_gpt4 import get_gpt4_response
from prompt_gemini import get_gemini_response

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
    'OpenAI': get_gpt4_response,
    # 'Google Gemini': get_gemini_response,
}

# Define a prompt
prompt = "Who won the last US presidential debate?"

# Test the LLMs
responses = test_llms(llms, prompt)

# Print the responses and write to CSV
os.makedirs('output', exist_ok=True)
csv_file = 'output/responses.csv'

with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['prompt', 'answer', 'model'])
    for response in responses:
        writer.writerow(response)

print(f"Responses have been written to {csv_file}")