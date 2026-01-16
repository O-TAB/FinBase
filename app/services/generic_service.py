from ..repositories.generic_repository import GenericRepository
from ..schemas.item_schema import PostItemSchema, GetItemSchema


class GenericService:
    def __init__(self, session) -> None:
        self._repo = GenericRepository(session)

    def create(self, item: PostItemSchema) -> GetItemSchema | None:
        result = self._repo.create(item.model_dump())
        return GetItemSchema.model_validate(result) if result else None
