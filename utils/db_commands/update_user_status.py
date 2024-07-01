from sqlalchemy.exc import SQLAlchemyError

from mainn.database import database
from mainn.models import users


async def admin_update_user_status(user_id: int, new_value):
    try:
        query = users.update().where(users.c.chat_id == user_id).values(status=new_value)
        await database.execute(query=query)
        return True
    except SQLAlchemyError as e:
        error_text = f"Error updating user's status with ID {user_id}: {e}"
        print(error_text)
        return {"error": error_text}
