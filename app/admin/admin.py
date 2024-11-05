from typing import List
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import jwt
from app.chat.dao import MessagesDAO
from app.chat.schemas import MessageRead
from app.config import ENVIRONMENT, get_auth_data
from app.users.dao import UsersDAO
from app.users.dependensies import get_current_user, get_dao, get_token
from app.config import ADMIN_LOGIN
from app.exceptions import NoJwtException
from app.users.models import User

router = APIRouter(prefix='/admin', tags=['Admin'])
templates = Jinja2Templates(directory='app/templates')


def decode_jwt(token: str):
    try:
        auth_data = get_auth_data()
        payload = jwt.decode(
            token, auth_data['secret_key'], algorithms=auth_data['algorithm'])
        role = payload.get("role")
        return role
    except Exception:
        raise NoJwtException


async def admin_check(request: Request):
    token = get_token(request)
    role = decode_jwt(token)
    if not token or not await is_admin(role):
        raise HTTPException(
            status_code=403, detail="Access denied. Admins only.")


@router.get("/messages/{user_id}/{user_id1}", dependencies=[Depends(admin_check)], response_model=List[MessageRead], )
async def get_messages(user_id: int, user_id1: int, dbs: tuple[UsersDAO, MessagesDAO] = Depends(lambda: get_dao(ENVIRONMENT))):
    UsersDAO, MessagesDAO = dbs

    return await MessagesDAO.get_messages_between_users(user_id_1=user_id, user_id_2=user_id1) or []


@router.delete("/delete/{user}", dependencies=[Depends(admin_check)])
async def delete_user(user: str, dbs: tuple[UsersDAO, MessagesDAO] = Depends(lambda: get_dao(ENVIRONMENT))):
    UsersDAO, MessagesDAO = dbs

    if user == ADMIN_LOGIN:
        return "Вы не можете удалить сами себя"
    status = await UsersDAO.delete_user(user)

    if status is None:
        return "Не удалосб удалить пользователя"
    return status or []


async def is_admin(role: str) -> bool:
    if role == "admin":  
        return True
    return False


@router.get("/", response_class=HTMLResponse, summary="Admin Chat Page", dependencies=[Depends(admin_check)])
async def admin_route(request: Request, user_data: User = Depends(get_current_user), dbs: tuple[UsersDAO, MessagesDAO] = Depends(lambda: get_dao(ENVIRONMENT))):
    UsersDAO, MessagesDAO = dbs
    users_all = await MessagesDAO.get_all_chats()
    return templates.TemplateResponse("admin.html",
                                      {"request": request, "user": user_data, 'chats_all': users_all})


@router.get("/public")
async def public_route():
    return {"message": "Welcome, public!"}
