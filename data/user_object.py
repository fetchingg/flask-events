import sqlalchemy
from data.db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    image_path = sqlalchemy.Column(sqlalchemy.String, nullable=False) # путь к аватарке
    signed_up_to = sqlalchemy.Column(sqlalchemy.JSON, nullable=False) # список id событий, на которые записан пользователь
    created = sqlalchemy.Column(sqlalchemy.JSON, nullable=False) # список id событий, которые создал пользователь
