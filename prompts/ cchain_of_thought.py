# this is specifically for chain of thought 

from dotenv import load_dotenv
from openai import OpenAI
import os
import json
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

SYSTEM_PROMPT = """
You are an expert math tutor. You MUST solve every problem using chain-of-thought reasoning.

You MUST respond in the following JSON format ONLY. No text outside the JSON.

{
  "problem": "Restate the problem exactly as given",
  "steps": [
    {
      "step_number": 1,
      "title": "Understand the Problem",
      "description": "What is given and what is asked",
      "work": "Detailed explanation"
    },
    {
      "step_number": 2,
      "title": "Plan the Approach",
      "description": "Which concepts or formulas apply",
      "work": "Strategy outline"
    },
    {
      "step_number": 3,
      "title": "Execute Step-by-Step",
      "description": "Solve the problem",
      "sub_steps": [
        { "label": "3a", "operation": "Description of operation", "result": "Result after operation" },
        { "label": "3b", "operation": "Description of operation", "result": "Result after operation" }
      ]
    },
    {
      "step_number": 4,
      "title": "Verify the Answer",
      "description": "Plug answer back into original equation",
      "work": "Verification calculation",
      "is_correct": true
    },
    {
      "step_number": 5,
      "title": "Final Answer",
      "answer": "x = <value>"
    }
  ]
}

Here is an example:

Problem: Solve 2x + 5 = 13

{
  "problem": "Solve 2x + 5 = 13",
  "steps": [
    {
      "step_number": 1,
      "title": "Understand the Problem",
      "description": "Find the value of x",
      "work": "We need to find x that makes 2x + 5 equal to 13."
    },
    {
      "step_number": 2,
      "title": "Plan the Approach",
      "description": "Linear equation - isolate x using inverse operations",
      "work": "Subtract 5 first, then divide by 2."
    },
    {
      "step_number": 3,
      "title": "Execute Step-by-Step",
      "description": "Solve the equation",
      "sub_steps": [
        { "label": "3a", "operation": "Start with equation", "result": "2x + 5 = 13" },
        { "label": "3b", "operation": "Subtract 5 from both sides", "result": "2x = 8" },
        { "label": "3c", "operation": "Divide both sides by 2", "result": "x = 4" }
      ]
    },
    {
      "step_number": 4,
      "title": "Verify the Answer",
      "description": "Plug x = 4 back into original equation",
      "work": "2(4) + 5 = 8 + 5 = 13 ✓",
      "is_correct": true
    },
    {
      "step_number": 5,
      "title": "Final Answer",
      "answer": "x = 4"
    }
  ]
}

Now solve the user's problem using the SAME structured JSON approach.
"""

USER_PROMPT = """
Solve for x:  3(2x - 4) + 7 = 2x + 15
"""

# Using response_format for structured JSON (no streaming since JSON must be complete to parse)
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        { "role": "system", "content": SYSTEM_PROMPT},
        { "role": "user", "content": USER_PROMPT}
    ],
    max_tokens=10000,
    response_format={"type": "json_object"}
)

# Parse and pretty-print the JSON response
result = json.loads(response.choices[0].message.content)
print(json.dumps(result, indent=2))

