import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai.errors import APIError

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
model = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in .env")

client = genai.Client(api_key=api_key)

chat = client.chats.create(
    model=model,
    config=types.GenerateContentConfig(
        system_instruction="You are a helpful assistant.",
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
                print("Assistant: The model returned no text response.\n")
                continue

            print(f"Assistant: {response.text}\n")

        except APIError as e:
            if e.code == 401:
                print("Error: Invalid Gemini API key.\n")
            elif e.code == 403:
                print("Error: Access to this Gemini model is forbidden.\n")
            elif e.code == 404:
                print(f"Error: Gemini model '{model}' was not found.\n")
            elif e.code == 429:
                print("Error: Gemini API rate limit or quota exceeded. Try again later.\n")
            elif e.code == 503:
                print("Error: Gemini model is temporarily unavailable or experiencing high demand. Try again later.\n")
            else:
                print(f"Gemini API error ({e.code}): {e.message}\n")

        except Exception as e:
            print(f"Error: {e}\n")

except KeyboardInterrupt:
    print("\nChat ended.")
