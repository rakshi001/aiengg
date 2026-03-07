import asyncio
import json
import aiohttp
import websockets


async def handle_client(websocket):
    async for message in websocket:
        print(f"\n📩 Received prompt: {message}")

        data = {
            "model": "qwen2.5-coder:7b",
            "prompt": message,
            "stream": True
        }

        full_response = ""
        async with aiohttp.ClientSession() as session:
            async with session.post("http://localhost:11434/api/generate", json=data) as resp:
                async for line in resp.content:
                    if line:
                        chunk = json.loads(line)
                        full_response += chunk["response"]

        print(f"✅ Response sent ({len(full_response)} chars)")
        await websocket.send(full_response)


async def main():
    async with websockets.serve(handle_client, "localhost", 8765):
        print("🚀 WebSocket server running on ws://localhost:8765")
        print("👉 Connect via Postman (WebSocket) and send a message!")
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
