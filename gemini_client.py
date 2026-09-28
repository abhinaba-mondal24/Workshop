import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai.errors import APIError

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in .env")

client = genai.Client(api_key=api_key)

chat = client.chats.create(
    model=model,
    config=types.GenerateContentConfig(
        system_instruction="You are a helpful technical assistant.",
        temperature=0.7,
        max_output_tokens=500
    )
)

print(f"Using model: {model}")
print("Type your question. Press Ctrl+C to exit.\n")

try:
    while True:
        question = input("You: ").strip()

        if not question:
            continue

        try:
            response = chat.send_message(question)

            if not response.text:
                print("Assistant: No response received.\n")
                continue

            print(f"Assistant: {response.text}\n")

        except APIError as e:
            print(f"Gemini API error: {e}\n")

except KeyboardInterrupt:
    print("\n\nChat ended.")
