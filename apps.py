from fastapi import FastAPI,Query,Body,Path
from schemas import *
from typing import List


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, data: str = None):
    return {"item_id": item_id, "data": data}

@app.get('/{id}')
def get_item(id: int, data: str = None):
    return{"Item": id, "data": data}



@app.get('/user/{id}/items/{item}/')
def get_user_item(id: int, item: str):
    return{"user":id, "item": item}


@app.post('/book')
def create_book(item:Book , author: Author , quantity: int=Body(...)):

    return {"item": item , "author": author , "quantity": quantity}




@app.post('/author')
def create_author(author:Author = Body(..., embed=True)):
    return{'author':author}



@app.get('/book')
def get_books(data:  List[str] = Query(['Test','Test2'], description="search book", deprecated=True)):
    return data