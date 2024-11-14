import requests

def get_openai_response(prompt, api_key):
    url = "https://api.openai.com/v1/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "text-davinci-003",
        "prompt": prompt,
        "max_tokens": 50
    }

    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code != 200:
        print("Failed to get a response from the API.")
        return None
    
    
    response_json = response.json()
    return response_json

def main():
    
    prompt = input("Enter your prompt for the OpenAI API: ")
    api_key = input("Enter your OpenAI API key: ")

   
    user_prompt = str(prompt)
    
  
    is_api_key_provided = bool(api_key)

    if not is_api_key_provided:
        print("API key is required. Exiting script.")
        return

    
    api_response = get_openai_response(user_prompt, api_key)

    if api_response is None:
        return

    # Extract and iterate over choices (list parsing)
    choices = api_response.get("choices", [])
    for idx, choice in enumerate(choices):
        # Dictionary parsing
        text_response = choice.get("text", "No response text")
        print(f"Response {idx + 1}: {text_response}")

    
    for i in range(3):
        print(f"Loop iteration {i + 1}: Example loop running")

    
    if len(choices) > 0:
        print("API returned valid responses.")


if __name__ == "__main__":
    main()
