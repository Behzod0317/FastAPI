from fastapi import FastAPI, Request
from googletrans import Translator
#from pydantic import BaseModel,validator,Field


app = FastAPI()


translator = Translator(service_urls=['https://translate.google.com/'])


@app.post("/translate")


async def translate_text(request: Request,  text: str ,dest_language: str):

    translated_text = translator.translate(text, dest=dest_language).text

  

    return {"text": translated_text}
    