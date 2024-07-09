import os
import pandas as pd
from prompt_gpt import get_gpt_responses
from prompt_gemini import get_gemini_responses

def test_llms(llms, prompts):
    responses = []
    for name, llm in llms.items():
        try:
            response_list = llm(prompts)
            responses.extend(response_list)  # Extend the list with the responses from each model
        except Exception as e:
            for prompt in prompts:
                responses.append((prompt, f"Error: {e}", name))
    return responses

# Define the LLMs to test
llms = {
    'OpenAI': get_gpt_responses,
    'Google Gemini': get_gemini_responses,
}

# Read the Excel file and extract the prompts
input_file = 'input/experiment_2.xlsx'
df_prompts = pd.read_excel(input_file)

# Extract prompts from the 'prompt_template' column
prompts = df_prompts['prompt_template'].tolist()

# Test the LLMs
responses = test_llms(llms, prompts)

# Write the responses to an Excel file
os.makedirs('output', exist_ok=True)
output_file = 'output/responses.xlsx'

df_responses = pd.DataFrame(responses, columns=['prompt', 'answer', 'model'])
df_responses.to_excel(output_file, index=False)

print(f"Responses have been written to {output_file}")