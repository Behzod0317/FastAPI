import requests
from fastapi import FastAPI


app = FastAPI()

@app.get("/weather/{city}")


async def get_weather(city: str):
    limit = 10
    api_key = "357eb9f4-a84c-11ed-a138-0242ac130002-357ebaee-a84c-11ed-a138-0242ac130002"
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={limit}&appid={api_key}"

    response = requests.get(url)


    if response.status_code == 200:

        return response.json()

    else:

        return {"error": "Ob-havo maʼlumotlarini olib boʻlmadi!"}
