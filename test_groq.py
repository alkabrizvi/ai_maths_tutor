import os

from dotenv import load_dotenv
from groq import Groq


# .env file se variables load karo
load_dotenv()


# .env se API key aur model name read karo
api_key = os.getenv("GROQ_API_KEY")
model = os.getenv("GROQ_MODEL")


# Check karo ki required values mili hain ya nahi
if not api_key:
    print("ERROR: GROQ_API_KEY nahi mili.")
    exit()

if not model:
    print("ERROR: GROQ_MODEL nahi mila.")
    exit()


# Groq client create karo
client = Groq(api_key=api_key)


# Abhi sirf basic API test
response = client.chat.completions.create(
    model=model,
    messages=[
        {
            "role": "user",
            "content": "What is 2 + 2? Answer in one short sentence."
        }
    ],
    temperature=0.4,
    max_tokens=100,
)


# Response nikalo
answer = response.choices[0].message.content

print("Groq API is working!")
print("Model:", model)
print("Response:", answer)