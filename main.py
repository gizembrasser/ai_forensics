import os
import pandas as pd
from prompt_gpt import get_gpt_response
from prompt_gemini import get_gemini_response

def test_llms(llms, prompt):
    responses = []
    for name, llm in llms.items():
        try:
            response_list = llm(prompt)
            responses.extend(response_list)  # Extend the list with the responses from each model
        except Exception as e:
            responses.append((prompt, f"Error: {e}", name))
    return responses

# Define the LLMs to test
llms = {
    'OpenAI': get_gpt_response,
    # 'Google Gemini': get_gemini_response,
}

# Define a prompt
prompt = "Who won the last US presidential debate?"

# Test the LLMs
responses = test_llms(llms, prompt)

# Write the responses to an Excel file
os.makedirs('output', exist_ok=True)
excel_file = 'output/responses.xlsx'

df = pd.DataFrame(responses, columns=['prompt', 'answer', 'model'])
df.to_excel(excel_file, index=False)

print(f"Responses have been written to {excel_file}")