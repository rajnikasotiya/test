import requests

def call_llm(prompt):
    api_key = 'your_openai_api_key'  # Replace with your actual API key
    url = 'https://api.openai.com/v1/chat/completions'

    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }

    data = {
        'model': 'gpt-3.5-turbo',  # Change this to the desired model
        'messages': [
            {'role': 'user', 'content': prompt}
        ],
        'max_tokens': 150,  # Adjust the max tokens as needed
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['message']['content']
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Example usage
if __name__ == "__main__":
    user_prompt = "What is the capital of France?"
    response = call_llm(user_prompt)
    print("LLM Response:", response)
