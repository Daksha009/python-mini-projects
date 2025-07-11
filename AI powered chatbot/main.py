import os
import openai
from openai import OpenAI

key = os.getenv("OPENAI_API_KEY") # Replace with your actual OpenAI API key


messages = [] 

client = OpenAI(
    # This is the default and can be omitted
    api_key=key,
    # You can also set the base URL if you are using a custom endpoint
)
def completion(message):
    global messages
    messages.append(
        {
            "role": "user",
          "content": message
          }
    )
    chat_completion = client.chat.completions.create( messages=messages,
                                  model = "gpt-4o"                   
                                                     )
    
    
    print(chat_completion)
    message = {
        "role": "assistant",
        "content": chat_completion.choices.message.content
    } 
    messages.append(message)
    print(f"Jarvis: {message.content}")
    
if __name__ == "__main__":
    print(f"Jarvis: Hii, I am Jarvis, How can I help you?\n")
    while True:
      user_question = input()
      print(f"User: {user_question}")
      completion(user_question)

    
