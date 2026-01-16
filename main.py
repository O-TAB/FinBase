from typing import Annotated
from fastapi import Depends, FastAPI
from pydantic import BaseModel
from uuid import UUID
from app.routers import catalog_router
from app.models import Base
from app.db import engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(catalog_router.router)


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


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons
