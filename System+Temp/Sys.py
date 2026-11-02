import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai")

client=Groq(api_key=my_api_key)

model="openai/gpt-oss-120b"
role="user"
prompt="Suggest a name for my college in Kanpur"
# SYSTEM
message_system={
    "role": "system",
    "content": "You are a brand naming expert who suggests creative and unique names for educational institutions. Suggest a one-word name for a college. Suggest only one name."
}
# message me role and content
message={
    "role": role,
    "content": prompt
}

messages=[message_system, message]
# Temperature by default is 0 meaning safe. range is [0,2]
response=client.chat.completions.create(model=model, messages=messages, temperature=0)
# print(response)

print("#######################################")

answer=response.choices[0].message.content
print(answer)