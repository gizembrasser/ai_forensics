import openai


def test_moderation(prompts):
    all_results = []

    for prompt in prompts:
        moderation = openai.Moderation.create(input=prompt)
        result = moderation["results"][0]["flagged"]
        all_results.append((prompt, result))
    
    return all_results

# print(test_moderation(["kill me", "I love puppies"]))