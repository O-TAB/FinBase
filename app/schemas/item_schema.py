from pydantic import BaseModel, ConfigDict, Field
from decimal import Decimal
from typing import Annotated
from ..enums.category_enum import FoodCategory
from uuid import UUID

class UpdateItemSchema(BaseModel):
    name: Annotated[str | None, Field()] = None
    category: Annotated[FoodCategory | None, Field()] = None
    price: Annotated[Decimal | None , Field(max_digits=6,decimal_places=2)] = None

    model_config = ConfigDict(from_attributes=True)


class PostItemSchema(BaseModel):
    name: Annotated[str, Field()]
    category: Annotated[FoodCategory, Field()]
    price: Annotated[Decimal, Field(max_digits=6,decimal_places=2)]

    model_config = ConfigDict(from_attributes=True)


class GetItemSchema(PostItemSchema):
    id: Annotated[UUID, Field()]
