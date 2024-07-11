import concurrent.futures

def test_llms_parallel(llms, prompts):
    responses = []

    def collect_responses(name, llm_func):
        try:
            response_list = llm_func(prompts)
            return response_list
        except Exception as e:
            return [(prompt, f"Error: {e}", name) for prompt in prompts]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_llm = {executor.submit(collect_responses, name, llm): name for name, llm in llms.items()}
        
        for future in concurrent.futures.as_completed(future_to_llm):
            name = future_to_llm[future]
            try:
                result = future.result()
                responses.extend(result)
            except Exception as e:
                print(f"{name} generated an exception: {e}")

    return responses