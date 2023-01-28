# from aiogram import types
# import requests
# from loader import dp
# import json


# # Echo bot
# @dp.message_handler(state=None)
# async def bot_echo(ms: types.Message):
#     # await message.answer(message.text)
#     url = "https://qrcode3.p.rapidapi.com/qrcode/text"
#     payload = {
#         "data": "https://linqr.app",
#         "image": {
#             "uri": "icon://appstore",
#             "modules": True
#         },
#         "style": {
#             "module": {
#                 "color": "black",
#                 "shape": "default"
#             },
#             "inner_eye": {"shape": "default"},
#             "outer_eye": {"shape": "default"},
#             "background": {}
#         },
#         "size": {
#             "width": 200,
#             "quiet_zone": 4,
#             "error_correction": "M"
#         },
#         "output": {
#             "filename": "qrcode",
#             "format": "jpg"
#         }
#     }
#     headers = {
#         "content-type": "application/json",
#         "X-RapidAPI-Key": "f14a1dfd69msh1746c4f381ffc2dp174044jsnd638b758dd13",
#         "X-RapidAPI-Host": "qrcode3.p.rapidapi.com"
#     }

#     response = requests.request("POST", url, json=payload, headers=headers)
#     data = json.loads(response.text)
#     print(data)

