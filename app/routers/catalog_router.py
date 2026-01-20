from uuid import UUID
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas.item_schema import PostItemSchema, GetItemSchema, UpdateItemSchema
from ..services.generic_service import GenericService
from ..db import get_db

router = APIRouter(prefix="/catalog", tags=["catalog"])


def get_service(session: Session = Depends(get_db)):
    return GenericService(session)


@router.get("/")
async def get_menu(
    service: GenericService = Depends(get_service)
):
    response = service.get_all()
    return response

@router.get("/{item_id}")
async def get_item(
    item_id: UUID, service: GenericService = Depends(get_service)
) -> GetItemSchema:
    response = service.get_by_id(item_id)
    if not response:
        raise ValueError
    return response
    
@router.post("/", response_model=GetItemSchema)
async def post_new_food(
    item: PostItemSchema, service: GenericService = Depends(get_service)
) -> GetItemSchema:
    response = service.create(item)
    if not response:
        raise ValueError
    return response


@router.patch("/{item_id}")
async def update_food(
    item_id: UUID, item: UpdateItemSchema, service: GenericService = Depends(get_service)
):
    response = service.update(item_id, item)
    if not response:
        raise ValueError
    return response
