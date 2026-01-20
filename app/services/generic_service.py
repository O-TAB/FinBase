from ..repositories.generic_repository import GenericRepository
from ..schemas.item_schema import PostItemSchema, GetItemSchema


class GenericService:
    def __init__(self, session) -> None:
        self._repo = GenericRepository(session)

    def create(self, item: PostItemSchema) -> GetItemSchema | None:
        result = self._repo.create(item.model_dump())
        return GetItemSchema.model_validate(result) if result else None
    
    def get_by_id(self, id)-> GetItemSchema | None:
        result = self._repo.get_by_id(id)
        return GetItemSchema.model_validate(result) if result else None
    
    def get_all(self):
        result = self._repo.get_all()
        items = {}
        items["itens"] = [GetItemSchema.model_validate(obj) for obj in result]
        return items
            

