from sqlalchemy import create_engine, MetaData, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

DB_URL = "sqlite://"

engine = create_engine(DB_URL, echo=True)

meta_ = MetaData()


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))


Base.metadata.create_all(engine)

with Session(engine) as session:
    user = User(name="welio")
    session.add(user)
    session.commit()

with Session(engine) as session:
    users = session.execute(session.query(User)).scalars().all()
    for user in users:
        print(f"id: {user.id}, name: {user.name}")
