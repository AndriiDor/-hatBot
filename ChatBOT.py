import openai
import os

client = openai.OpenAI(api_key=os.getenv("YOUR_API"))

def chat():
    print("Welcome to your ChatGPT-powered assistant! Type 'exit' to quit.")
    messages = [{"role": "system", "content": "You are a helpful assistant."}]

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        messages.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            reply = response.choices[0].message.content
            print("Bot:", reply)
            messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            print("Error:", e)

chat()
