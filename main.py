from fastapi import FastAPI
from pydantic import BaseModel
from uuid import UUID

app = FastAPI()


class Order(BaseModel):
    id: UUID 
    oders: dict
    totalprice: int


@app.get("/")
def root():
    return {"mensage": "Hello World"}

@app.post("/order/")
def save_order(Item: Order):
    return Item.model_dump()

@app.options("/itens/")
def options_avalible():
    pass

