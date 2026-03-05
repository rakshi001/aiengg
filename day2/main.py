from fastapi import FastAPI
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


@app.get("/")
def home():
    return {"message": "FastAPI + Gemini running"}


@app.get("/ask")
def ask_llm(question: str):
    response = model.generate_content(question)
    return {"answer": response.text}
