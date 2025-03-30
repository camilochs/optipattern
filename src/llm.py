import anthropic
import openai

def execute_anthropic(prompt, api_key, model="claude-3-opus-20240229"):
    client = anthropic.Anthropic(api_key=api_key)
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ]
    )
    return message.content[0].text

def execute_openai(prompt, api_key, model="gpt-4o"):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000,
        temperature=0,
    )
    return response.choices[0].message["content"]

def execute_llm(prompt_file, api_key, provider="anthropic", model="claude-3-opus-20240229"):
    with open(prompt_file, "r") as f:
        prompt = f.read()
        if provider.lower() == "anthropic":
            return execute_anthropic(prompt, api_key, model=model)
        elif provider.lower() == "openai":
            return execute_openai(prompt, api_key, model=model)
        else:
            raise ValueError("Provider must be either 'anthropic' or 'openai'")
