# OpenAI and Gemini API with Python

Simple Python examples for accessing OpenAI GPT models and Google Gemini models using API keys.

The OpenAI example also supports **OpenAI-compatible APIs** by changing the API base URL.

## Setup

Create a virtual environment and install the dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file from `.env.example`:

```bash
cp .env.example .env
```

Add your API keys to `.env`.

## OpenAI

The OpenAI example uses:

```env
OPENAI_API_KEY=your_openai_api_key
OPENAI_BASE_URL=https://api.openai.com/v1
OPENAI_MODEL=gpt-5
```

Run:

```bash
python openai_client.py
```

### OpenAI-Compatible Endpoint

The OpenAI Python SDK allows the API base URL to be changed.

For an OpenAI-compatible provider, change:

```env
OPENAI_API_KEY=your_provider_api_key
OPENAI_BASE_URL=https://your-provider.com/v1
OPENAI_MODEL=your-model
```

The Python code remains the same.

For example, a locally hosted OpenAI-compatible server could use:

```env
OPENAI_BASE_URL=http://localhost:8000/v1
OPENAI_MODEL=your-local-model
```

The exact URL and model name depend on the provider or server.

## Gemini

The Gemini example uses Google's `google-genai` SDK.

Configure:

```env
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-3.8-flash
```

Run:

```bash
python gemini_client.py
```

## Files

```text
openai_client.py
gemini_client.py
requirements.txt
.env.example
README.md
```

Do not upload your actual `.env` file or API keys to GitHub.