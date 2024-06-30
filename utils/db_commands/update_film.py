from sqlalchemy.exc import SQLAlchemyError

from main.database import database
from main.models import films


async def admin_update_film(film_id: int, column: str, new_value):
    try:
        query = films.update().where(films.c.id == film_id).values({column: new_value})
        await database.execute(query=query)
        return True
    except SQLAlchemyError as e:
        error_text = f"Error updating film with ID {film_id}: {e}"
        print(error_text)
        return {"error": error_text}


async def admin_update_film_date(film_id: int, new_value: int):
    try:
        query = films.update().where(films.c.id == film_id).values(date=new_value)
        await database.execute(query=query)
        return True
    except SQLAlchemyError as e:
        error_text = f"Error updating film with ID {film_id}: {e}"
        print(error_text)
        return {"error": error_text}


async def admin_delete_film(film_id: int):
    try:
        query = films.delete().where(films.c.id == film_id)
        await database.execute(query=query)
        return True
    except SQLAlchemyError as e:
        error_text = f"Error updating film with ID {film_id}: {e}"
        print(error_text)
        return {"error": error_text}



