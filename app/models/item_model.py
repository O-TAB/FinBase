from decimal import Decimal
from .base_model import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Numeric, UUID
import uuid


class ItemModel(Base):
    __tablename__ = "item"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(String(100))
    category: Mapped[str] = mapped_column(String(100))
    price: Mapped[Decimal] = mapped_column(Numeric)
