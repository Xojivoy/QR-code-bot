from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

statr = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("QR kod yaratish"),
            # KeyboardButton("")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)