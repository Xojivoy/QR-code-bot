import requests
from loader import dp 
from aiogram.types import Message
import json
@dp.message_handler()
async def jonatti(ms : Message):
    url = "https://easy-qr-code-generator.p.rapidapi.com/v1/generateqr"

    querystring = {"text":"https://en.wikipedia.org/wiki/Nikola_Tesla","width":"200"}

    headers = {
        "X-RapidAPI-Key": "f14a1dfd69msh1746c4f381ffc2dp174044jsnd638b758dd13",
        "X-RapidAPI-Host": "easy-qr-code-generator.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    dataa = json.loads(response.text)
    print(dataa)
    rasmi = dataa['data']
    msg = "QR kod tayyor bo'ldi!\n"
    msg+= "\nKodni @qrcode_maytext_bot yaratdi"
    await ms.answer_photo(rasmi, caption=msg)
    # print(response.)