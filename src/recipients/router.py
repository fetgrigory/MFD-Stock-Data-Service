'''
This module make

Author: Fetkulin Grigory, Fetkulin.G.R@yandex.ru
Starting 30/09/2025
Ending //

'''
# Installing the necessary libraries
from fastapi import APIRouter, Path, Query, HTTPException
import psycopg2
from psycopg2 import errorcodes
from src.database import insert_recipient_data, update_recipient_data, delete_recipient_data

router = APIRouter(tags=["Пользователи 👤"])


# Endpoint for adding a new recipient
@router.post(
    "/recipients",
    tags=["Получатели 👤"],
    summary="Добавить нового получателя",
    status_code=201
)
def create_recipient(
    name: str = Query(..., description="Имя получателя"),
    email: str = Query(..., description="Email получателя")
):
    try:
        recipient_id = insert_recipient_data(name, email)
        return {"id": recipient_id, "Имя": name, "Адрес электронной почты": email}

    except psycopg2.Error as e:
        if e.pgcode == errorcodes.UNIQUE_VIOLATION:
            raise HTTPException(status_code=400, detail="Получатель с таким email уже существует") from e
        else:
            raise


# Endpoint for update recipient
@router.patch(
    "/recipients/{recipient_id}",
    tags=["Получатели 👤"],
    summary="Обновить данные получателя",
    status_code=200
)
def update_recipient(
    recipient_id: int = Path(..., description="ID получателя для обновления"),
    name: str | None = Query(None, description="Новое имя получателя"),
    email: str | None = Query(None, description="Новый email получателя")
):
    if name is None and email is None:
        raise HTTPException(status_code=400, detail="Необходимо указать хотя бы одно поле для обновления")
    try:
        updated_recipient = update_recipient_data(recipient_id, name, email)
        if not updated_recipient:
            raise HTTPException(status_code=404, detail="Получатель не найден")
        return {"id": recipient_id, "Имя": updated_recipient["name"], "Email": updated_recipient["email"]}

    except psycopg2.Error as e:
        if e.pgcode == errorcodes.UNIQUE_VIOLATION:
            raise HTTPException(status_code=400, detail="Получатель с таким email уже существует") from e
        else:
            raise


# Endpoint for deleting a recipient by ID
@router.delete(
    "/recipients/{recipient_id}",
    tags=["Получатели 👤"],
    summary="Удалить получателя по ID",
    status_code=200
)
def delete_recipient(recipient_id: int = Path(..., description="ID получателя для удаления")):
    deleted_count = delete_recipient_data(recipient_id)
    if deleted_count == 0:
        raise HTTPException(status_code=404, detail="Получатель не найден")
    return {"message": f"Получатель с ID {recipient_id} успешно удален"}
