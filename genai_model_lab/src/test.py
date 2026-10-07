from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

load_dotenv()

app = FastAPI()

@app.get("/")
def greet():
    return "Hello"

class Review(BaseModel):
    text: str

class Response_format(BaseModel):
    label: str
    score: int
    theme: str

@app.post("/analyze")
def analyze(Review):
    client = OpenAI()

    response = client.beta.chat.completions.parse(
        model="gpt-5.5",
        messages=[
            {"role": "system", "content": "Analyze this customer review. label must be 'positive', 'negative', or 'neutral' score must be a number from 1 (very bad) to 5 (very good). theme must be ONE lowercase word for the main topic. (for example: delivery, taste, price, service, quality)."},
            {"role": "user", "content": f"Review: {Review}"}
        ],
        response_format=Response_format
    )

    return response.choices[0].message.parsed

new =  analyze("this is a bad product")
print(new)