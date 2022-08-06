from aiogram import types
from loader import dp


@dp.message_handler(text="ID")
async def send_user_id(message: types.Message):
    id = message.from_user.id
    await message.answer(f"Sizning ID: {id}")


@dp.message_handler(text="Username")
async def send_user_id(message: types.Message):
    username = message.from_user.username
    await message.answer(f"Sizning username: {username}")


@dp.message_handler(text="First Name")
async def send_user_id(message: types.Message):
    first_name = message.from_user.first_name
    await message.answer(f"Sizning ismingiz: {first_name}")


@dp.message_handler(text="Last Name")
async def send_user_id(message: types.Message):
    last_name = message.from_user.last_name
    await message.answer(f"Sizning familyangiz: {last_name}")