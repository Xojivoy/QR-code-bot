from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.keys import statr
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}!\nMen siz yozgan matnga QR kod qilib beraman.\n QR code yaratish uchun shunchaki matn yoki url yuboring !", reply_markup=statr)

@dp.message_handler(text='QR kod yaratish')
async def yordamber(ms : types.Message):
    await ms.answer("QR code yaratish uchun shunchaki matn yoki url yuboring !")
