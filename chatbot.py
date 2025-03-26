import requests
import json
import base64
from prompt import format_prompt 


encoded_url = "aHR0cDovLzE5Mi4xNjguMS4xMjc6MTIzNC92MS9jaGF0L2NvbXBsZXRpb25z" 

url = base64.b64decode(encoded_url).decode()

headers = {"Content-Type": "application/json"}


def chat_with_phi2(user_input):
    formatted_input = format_prompt(user_input) 

    data = {
        "model": "phi-2",
        "messages": [
            {"role": "user", "content": formatted_input}
        ],
        "temperature": 0.7,
        "max_tokens": 8000 ,
        "stream": False
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data),timeout= 25)
        response.raise_for_status()  
        response = response.json().get("choices", [{}])[0].get("message", {}).get("content", "").strip()
        print("Response: ", response)
        return response
    except requests.exceptions.Timeout:
        return "API Timeout: The server took too long to respond."
    except requests.exceptions.ConnectionError:
        return "Connection Error: Unable to reach the API."
    except requests.exceptions.HTTPError as e:
        return f"HTTP Error: {e}"
    except Exception as e:
        return f"Unexpected Error: {e}"
    
    
def run_chatbot():

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        bot_response = chat_with_phi2(user_input)
        print(f"Bot: {bot_response}")


if __name__ == "__main__":
    run_chatbot()
    
