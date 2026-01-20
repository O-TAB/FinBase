
from sqlite3 import IntegrityError
from sqlalchemy.orm import Session
from sqlalchemy import select, update
from ..models.item_model import ItemModel
from typing import Type


class GenericRepository:
    def __init__(self, session) -> None:
        self._session: Session = session
        self._model: Type[ItemModel] = ItemModel

    def create(self, data: dict):
        item = self._model(**data)
        self._session.add(item)
        self._session.commit()
        self._session.refresh(item)
        return item

    def get_by_id(self, id):
        item = self._session.get(self._model,id)
        return item
    
    def get_all(self):
        result = self._session.scalars(select(self._model)).all()
        return result
    
    def update(self, id, payload: dict):
        stmt = update(self._model).where(self._model.id == id).values(**payload).returning(self._model)
        try: 
            result = self._session.execute(stmt).scalar_one()
            self._session.commit()
            return result
        except IntegrityError as e:
            self._session.rollback()
            raise e
        

