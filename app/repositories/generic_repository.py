from sqlalchemy.orm import Session
from ..models.item_model import ItemModel


class GenericRepository:
    def __init__(self, session) -> None:
        self._session: Session = session
        # self._model: ItemModel

    def create(self, data):
        item = ItemModel(**data)
        self._session.add(item)
        self._session.commit()
        self._session.refresh(item)
        return item
