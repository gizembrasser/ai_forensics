from openai import OpenAI

client = OpenAI(
api_key = "<your_llamaapi_token>",
base_url = "https://api.llama-api.com"
)

def get_llama_responses(prompts):
    all_responses = []

    for prompt in prompts:
        response = client.chat.completions.create(
        model="llama-13b-chat",
        messages=[
            {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
            {"role": "user", "content": prompt}
        ]   
        )

        print(response.model_dump_json(indent=2))
        print(response.choices[0].message.content)
        


            