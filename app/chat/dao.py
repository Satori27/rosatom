from sqlalchemy import select, and_, or_
from app.dao.base import BaseDAO
from app.chat.models import Message
from app.database import async_session_maker as async_session
from sqlalchemy import text


class MessagesDAO(BaseDAO):
    model = Message
    async_session_maker = async_session

    @classmethod
    async def get_messages_between_users(cls, user_id_1: int, user_id_2: int):
        """
        Асинхронно находит и возвращает все сообщения между двумя пользователями.

        Аргументы:
            user_id_1: ID первого пользователя.
            user_id_2: ID второго пользователя.

        Возвращает:
            Список сообщений между двумя пользователями.
        """
        async with cls.async_session_maker() as session:
            query = select(cls.model).filter(
                or_(
                    and_(cls.model.sender_id == user_id_1, cls.model.recipient_id == user_id_2),
                    and_(cls.model.sender_id == user_id_2, cls.model.recipient_id == user_id_1)
                )
            ).order_by(cls.model.id)
            result = await session.execute(query)
            return result.scalars().all()
    
    @classmethod
    async def get_all_chats(cls):
        async with cls.async_session_maker() as session:
            cross_join_query = text("SELECT a.id, a.name, b.id, b.name FROM users AS a, users AS b WHERE a.id < b.id")

            result = await session.execute(cross_join_query)
        
            chats_list = [
                {
                    "sender_id": chat[0],
                    "sender_name": chat[1],
                    "recipient_id": chat[2],
                    "reciever_name": chat[3]
                }
                for chat in result.all()
            ]

            return chats_list