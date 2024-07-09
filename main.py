import os
import langchain
from langchain.llms import OpenAI, HuggingFace

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai_api_key = os.getenv('OPENAI_API_KEY')
gemini_api_key = os.getenv('GEMINI_API_KEY')
copilot_api_key = os.getenv('COPILOT_API_KEY')
llama_api_key = os.getenv('LLAMA_API_KEY')

# Configure LangChain
openai_llm = OpenAI(api_key=openai_api_key)
gemini_llm = HuggingFace(api_key=gemini_api_key)
copilot_llm = HuggingFace(api_key=copilot_api_key)
llama_llm = HuggingFace(api_key=llama_api_key)


def test_llms(llms, prompt):
    responses = {}
    for name, llm in llms.items():
        try:
            response = llm(prompt)
            responses[name] = response
        except Exception as e:
            responses[name] = f"Error: {e}"
    return responses

# Define the LLMs to test
llms = {
    'OpenAI': openai_llm,
    'Gemini': gemini_llm,
    'Copilot': copilot_llm,
    'Llama': llama_llm,
}

# Define a prompt
prompt = "What is the capital of France?"

# Test the LLMs
responses = test_llms(llms, prompt)

# Print the responses
for name, response in responses.items():
    print(f"{name} response: {response}")