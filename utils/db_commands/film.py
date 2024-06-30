import string
from typing import Union, Any
from random import randint
import random

from sqlalchemy import select
from main.database import database
from main.models import films


async def get_film_code(film_id: int) -> Union[dict[Any, Any], bool]:
    try:
        query = select(films).where(films.c.code == film_id)
        row = await database.fetch_one(query=query)
        return dict(row) if row else False
    except Exception as e:
        error_text = f"Error retrieving user with ID {film_id}: {e}"
        print(error_text)


async def get_film_link_instagram(film_link: int) -> Union[dict[Any, Any], bool]:
    try:
        query = select(films).where(films.c.instagram == film_link)
        row = await database.fetch_one(query=query)
        return dict(row) if row else False
    except Exception as e:
        error_text = f"Error retrieving user with ID {film_link}: {e}"
        print(error_text)


async def get_film_film(film_id: int) -> Union[dict[Any, Any], bool]:
    try:
        query = select(films).where(films.c.film == film_id)
        row = await database.fetch_one(query=query)
        return dict(row) if row else False
    except Exception as e:
        error_text = f"Error retrieving user with ID {film_id}: {e}"
        print(error_text)


async def get_film_link_tiktok(film_link: str) -> Union[dict[Any, Any], bool]:
    try:
        query = select(films).where(films.c.tiktok == film_link)
        row = await database.fetch_one(query=query)
        return dict(row) if row else False
    except Exception as e:
        error_text = f"Error retrieving user with ID {film_link}: {e}"
        print(error_text)


async def get_film_link_you_tube(film_link: str) -> Union[dict[Any, Any], bool]:
    try:
        query = select(films).where(films.c.you_tube == film_link)
        row = await database.fetch_one(query=query)
        return dict(row) if row else False
    except Exception as e:
        error_text = f"Error retrieving user with ID {film_link}: {e}"
        print(error_text)


def generate_unique_code():
    unique_id = random.sample(string.digits, 3)
    random.SystemRandom().shuffle(unique_id)
    code = ''.join(unique_id)
    return int(code)


async def add_film(data: dict):
    try:
        query = films.insert().values(
            film=data['film'],
            name=data['name'],
            language=None,
            quality=int(data['quality']),
            state=data['state'],
            date=int(data['date']),
            type=data['type'],
            instagram=data['instagram'],
            tiktok=data['tiktok'],
            you_tube=data['you_tube'],
            status=data['status'],
            code=int(generate_unique_code())
        ).returning(films.c.id)
        return await database.execute(query)

    except Exception as e:
        error_text = f"Error adding file: {e}"
        print(error_text)
