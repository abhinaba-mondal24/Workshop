import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
model = os.getenv("OPENAI_MODEL", "gpt-5")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in .env")

client = OpenAI(
    api_key=api_key,
    base_url=base_url
)

messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant."
    }
]

print(f"Using model: {model}")
print("Type your question. Press Ctrl+C to exit.\n")

try:
    while True:
        question = input("You: ").strip()

        if not question:
            continue

        messages.append({
            "role": "user",
            "content": question
        })

        try:
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0.7,
                max_tokens=500
            )

            if not response.choices:
                print("Assistant: No response received.\n")
                messages.pop()
                continue

            message = response.choices[0].message
            answer = message.content

            if answer is None:
                print("Assistant: The model returned no text response.\n")
                messages.pop()
                continue

            print(f"Assistant: {answer}\n")

            messages.append({
                "role": "assistant",
                "content": answer
            })

        except Exception as e:
            print(f"API error: {e}\n")
            messages.pop()

except KeyboardInterrupt:
    print("\nChat ended.")
