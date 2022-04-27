from aiogram.types import Message as msg

from config import bot,db
from bot_database import *
from texts import main_texts
from keys import keyboards_lang,language_to_change

async def fix_settings(message: msg, step: int):
    user_id = message.from_user.id
    text = message.text
    lang = await db.get_user_data('language','customers','user_id',user_id)
    lang = lang[0]
    if step == 12:
        await bot.send_message(user_id,main_texts[lang]["What do you change"],reply_markup=keyboards_lang[lang]["change"])
        await db.update_column_values(user_id,'step',13)
    elif step == 13:
        if text == "Tilni o'zgartirish 🇺🇿" or text == "Изменить язык 🇷🇺":
            await bot.send_message(user_id,main_texts[lang]["Choose language"], reply_markup=language_to_change)
        elif text == "Telefon raqam 📱" or text == "Телефон номер 📱":
            await db.update_column_values(user_id,'step',14)
            await bot.send_message(user_id,main_texts[lang]["Ex phone number"])
        elif text == "🔙Orqaga" or text == "🔙Назад":
            await bot.send_message(user_id,main_texts[lang]["Base menu"],reply_markup=keyboards_lang[lang]["Base buttons"])
    elif step == 14:
        if len(text) == 13 or text[0] == "+":
            await bot.send_message(user_id,main_texts[lang]["Data changed"],reply_markup=keyboards_lang[lang]["Base buttons"])
            await db.update_column_values(user_id,'phone_number',text)
        elif len(text) == 12:
            await bot.send_message(user_id,main_texts[lang]["Data changed"],reply_markup=keyboards_lang[lang]["Base buttons"])
            await db.update_column_values(user_id,'phone_number',text)
        elif text == "🔙Orqaga" or text == "🔙Назад":
            await bot.send_message(user_id,main_texts[lang]["Base menu"],reply_markup=keyboards_lang[lang]["Base buttons"])
        else:
            await bot.send_message(user_id,main_texts[lang]["Entered wrong"])
            await bot.send_message(user_id,main_texts[lang]["Ex phone number"])
    elif step == 15:
        if text.isdigit():
            await db.update_column_values(user_id,'card_numbers',text)
            await bot.send_photo(user_id,open("freenught.jpeg"))
            await bot.send_message(user_id,main_texts[lang]["After sended photo"])
