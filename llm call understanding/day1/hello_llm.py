import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
load_dotenv()
my_api_key=os.getenv("GROQ-API-Key")
if not my_api_key:
    raise ValueError("API-Error")
client=Groq(api_key = my_api_key)
model = "llama-3.3-70b-versatile"
role="user"
prompt = "Do you know kritika"
message = {
    "role":role,
    "content":prompt
}
messages=[message]
response = client.chat.completion.create (model = model,messages=message)
print(response)