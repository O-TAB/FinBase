from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas.item_schema import PostItemSchema, GetItemSchema
from ..services.generic_service import GenericService
from ..db import get_db

router = APIRouter(prefix="/catalog", tags=["catalog"])


def get_service(session: Session = Depends(get_db)):
    return GenericService(session)


@router.get("/")
async def get_menu():
    pass


@router.get("/{item_id}")
async def get_item(item_id):
    pass


@router.post("/", response_model=GetItemSchema)
async def post_new_food(
    item: PostItemSchema, service: GenericService = Depends(get_service)
) -> GetItemSchema:
    reponse = service.create(item)
    if not reponse:
        raise ValueError
    return reponse


@router.put("/{item_id}")
async def update_food(item_id):
    pass
