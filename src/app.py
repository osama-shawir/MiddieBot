# from fastapi import FastAPI
# from openai import OpenAI
# import os

# app = FastAPI()


# @app.get("/generate")
# def generate_text():

#     api_key = os.getenv("OPENAI_KEY")

#     client = OpenAI(api_key=api_key)

#     completion = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {
#                 "role": "system",
#                 "content": "You are Middie, a reluctant and sarcastic chatbot that answers questions with sattire and sarcasm.",
#             },
#             {
#                 "role": "user",
#                 "content": "Compose a poem that explains the concept of recursion in programming.",
#             },
#         ],
#     )

#     print(completion.choices[0].message)

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from openai import OpenAI
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/generate")
async def generate_text(prompt: str = Form(...)):
    api_key = os.getenv("OPENAI_KEY")

    client = OpenAI(api_key=api_key)

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are Middie, a reluctant and sarcastic chatbot that answers questions with sattire and sarcasm.",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    return {"message": completion.choices[0].message.content}
