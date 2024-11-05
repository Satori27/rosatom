from app.chat.dao import MessagesDAO
from app.users.dao import UsersDAO
from tests.database import test_async_session_maker as async_session


class TestUsersDAO(UsersDAO):
    async_session_maker = async_session


class TestMessagesDAO(MessagesDAO):
    async_session_maker = async_session
