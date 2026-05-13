import sqlalchemy
from sqlalchemy_serializer import SerializerMixin

from data.db_session import SqlAlchemyBase


class User(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    email = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    image_path = sqlalchemy.Column(sqlalchemy.String, nullable=True) # путь к аватарке
    signed_up_to = sqlalchemy.Column(sqlalchemy.JSON, nullable=True) # список id событий, на которые записан пользователь
    created = sqlalchemy.Column(sqlalchemy.JSON, nullable=True) # список id событий, которые создал пользователь
