import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai")

client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-120b"
role = "user"
prompt = "Suggest a name for my college in Kanpur"

message_system = {
    "role": "system",
    "content": (
        "You are a brand naming expert who suggests creative and unique names "
        "for educational institutions. Suggest a one-word name for a college "
        "located in Kanpur. Suggest only one name."
    ),
}
message = {
    "role": role,
    "content": prompt,
}

messages = [message_system, message]
response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=0,
)

print("#######################################")
print(response.choices[0].message.content)
