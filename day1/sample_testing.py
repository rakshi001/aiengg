import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

# Initialize the OpenAI client pointing to Google's Gemini API
# It will use the OPENAI_API_KEY environment variable. We set it in .env to the Gemini API Key
api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
if not api_key:
    print("Error: GOOGLE_API_KEY is not set in the .env file.")
    exit(1)

client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def test_openai_api():
    try:
        print("Sending request to OpenAI API...")
        
        # Using gemini-2.5-flash as it's Google's fast, capable, and cost-effective model
        response = client.chat.completions.create(
            model="gemini-2.5-flash",
            messages=[
                {"role": "system", "content": "You are a helpful, enthusiastic assistant."},
                {"role": "user", "content": "Please tell me about the history of AI"}
            ],
            max_tokens=100000
        )
        
        print("\n=== API Connection Successful! ===")
        print(f"Message: {response.choices[0].message.content}")
        print("==================================")
        
    except Exception as e:
        print(f"\n=== Error ===")
        print(f"Failed to connect or generate response: {e}")
        print("\nPlease ensure that:")
        print("1. You have set the GEMINI_API_KEY environment variable in your .env file.")
        print("2. Your API key is valid.")

if __name__ == "__main__":
    test_openai_api()
