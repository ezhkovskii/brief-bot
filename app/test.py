from g4f.client import Client
from g4f.Provider import BingCreateImages, OpenaiChat, Gemini

client = Client()
model = "gpt-3.5-turbo"

messages = []
while True:
    user_message = input()
    messages.append({"role": "user", "content": user_message})
    completion = client.chat.completions.create(
        model=model,
        messages=messages
    )
    completion_choices_item = completion.choices[0].to_json()
    messages.append(completion_choices_item["message"])
    print(completion.choices[0].message.content)