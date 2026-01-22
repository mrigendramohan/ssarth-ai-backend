from fastapi import FastAPI
from openai import OpenAI
import os

app = FastAPI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.post("/chat")
async def chat(data: dict):
    user_msg = data.get("message")

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are SSArth AI assistant helping users find local services."},
            {"role": "user", "content": user_msg}
        ]
    )

    return {"reply": response.choices[0].message.content}
