import json
import aiohttp
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

OLLAMA_URL = "http://localhost:11434/api/generate"


class Prompt(BaseModel):
    prompt: str


@app.post("/generate")
async def generate(prompt: Prompt):

    payload = {
        "model": "qwen2.5-coder:7b",
        "prompt": prompt.prompt,
        "stream": True
    }

    full_response = ""

    async with aiohttp.ClientSession() as session:
        async with session.post(OLLAMA_URL, json=payload) as resp:

            async for line in resp.content:
                if not line:
                    continue

                chunk = json.loads(line.decode())

                if "response" in chunk:
                    full_response += chunk["response"]

                if chunk.get("done"):
                    break

    return {"response": full_response}