from typing import Any, Union

from sqlalchemy.exc import SQLAlchemyError

from main.database import database
from main.models import *


async def get_user(chat_id: int) -> Union[dict[Any, Any], bool]:
    try:
        query = users.select().where(users.c.chat_id == chat_id)
        row = await database.fetch_one(query=query)
        return dict(row) if row else False
    except Exception as e:
        error_text = f"Error get user with ID {chat_id}: {e}"
        print(error_text)


async def get_user_language(chat_id: int) -> Union[dict[Any, Any], bool]:
    try:
        query = users.select().where(users.c.chat_id == chat_id)
        row = await database.fetch_one(query=query)
        return dict(row) if row else False
    except Exception as e:
        error_text = f"Error retrieving user with ID {chat_id}: {e}"
        print(error_text)


async def update_user_language(chat_id: int, language: str):
    try:
        query = users.update().where(users.c.chat_id == chat_id).values(language=language)
        await database.execute(query=query)
        return True
    except SQLAlchemyError as e:
        error_text = f"Error changing user's language with ID {chat_id}: {e}"
        print(error_text)
        return {"error": error_text}


async def get_user_status(chat_id: int):
    try:
        query = users.select().where(users.c.chat_id == chat_id)
        row = await database.fetch_one(query=query)
        return dict(row)["status"] if row else False
    except Exception as e:
        error_text = f"Error retrieving user with ID {chat_id}: {e}"
        print(error_text)


async def add_user(data: dict, message):
    try:
        query = users.insert().values(
            chat_id=message.chat.id,
            language=data['language'],
            status="Free"
        )
        await database.execute(query)
        return True
    except Exception as e:
        error_text = f"Error adding user: {e}"
        print(error_text)


async def add_admin_table_user(data: dict, message):
    try:
        query = users.insert().values(
            chat_id=message.chat.id,
            language=data['language'],
            status="Admin"
        )
        await database.execute(query)
        return True
    except Exception as e:
        error_text = f"Error adding admin: {e}"
        print(error_text)
