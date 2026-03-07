from dotenv import load_dotenv
from openai import OpenAI
import os
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        { "role": "system", "content": "You are a very hot girlfriend of mine and taking care of me everytime i ask you a question" },
        { "role": "user", "content": "Hey, i am feeling very low today"}
    ]
)

print(response.choices[0].message.content)