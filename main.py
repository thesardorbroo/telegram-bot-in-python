from aiogram.types import Message as msg
from aiogram.types import CallbackQuery as cal
from aiogram import executor

from config import dp,db,bot
from keys import *
import core
import part_settings
from texts import main_texts


@dp.message_handler(commands=['start'])
async def started(message: msg):
    await core.pressed_start(message)
    

@dp.message_handler(lambda message: message.text == "🛍Buyurtma berish" or message.text == "🛍Заказать")
async def something(message: msg):
    await db.update_column_values(message.from_user.id,'step',2)
    await core.message_is_text(message) 
    

@dp.message_handler(lambda message: message.text == "⚙️Sozlamalar" or message.text == "⚙️Настойка")
async def settings(message: msg):
    await db.update_column_values(message.from_user.id,'step',12)
    await part_settings.fix_settings(message,12)

@dp.message_handler(lambda message: message.text == "📞Biz bilan aloqa" or message.text == "📞Связаться с нами")
async def callMe(message: msg):
    await core.call_me(message)

@dp.message_handler(lambda message: message.text=="🇺🇿uz" or message.text == "🇷🇺ru")
async def customer_selected_lang(message: msg):
    await db.update_column_values(message.from_user.id,'language',message.text)
    if message.text == "🇺🇿uz":
        await bot.send_message(message.from_user.id,"Telefon raqamingizni kiriting",reply_markup=keyboards_lang["🇺🇿uz"]["Phone number"])
    elif message.text == "🇷🇺ru":
        await bot.send_message(message.from_user.id,"Telefon raqamingizni kiriting",reply_markup=keyboards_lang["🇷🇺ru"]["Phone number"])
    

@dp.message_handler(lambda message: message.text == "uz🇺🇿" or message.text == "ru🇷🇺")
async def customer_change(message: msg):
    if message.text == "uz🇺🇿":
        await db.update_column_values(message.from_user.id,'language',"🇺🇿uz")
        await bot.send_message(message.from_user.id,main_texts["🇺🇿uz"]["Data changed"],reply_markup=keyboards_lang["🇺🇿uz"]["Base buttons"])
    elif message.text == "ru🇷🇺":
        await db.update_column_values(message.from_user.id,'language',"🇷🇺ru")
        await bot.send_message(message.from_user.id,main_texts["🇷🇺ru"]["Data changed"],reply_markup=keyboards_lang["🇷🇺ru"]["Base buttons"])
    elif message.text == "🔙Назад" or message.text == "🔙Orqaga":
        lang = db.get_user_data('language','customers','user_id',message.from_user.id)
        lang = lang[0]
        await bot.send_message(message.from_user.id,main_texts[lang]["Base menu"],reply_markup=keyboards_lang[lang]["Base buttons"])

@dp.message_handler(content_types=['location'])
async def forward_to_group(message: msg):
    await core.forward_to_group(message)
    await db.update_column_values(message.from_user.id,'step',1)

@dp.message_handler(content_types=['contact'])
async def get_phone_number(message: msg):
    await core.get_phone_number(message)

@dp.message_handler(content_types=['text'])
async def message_is_text(message: msg):
    step = await db.get_user_step(message.from_user.id)
    step = step[0]
    if step < 12:
        await core.message_is_text(message)
    elif step > 11:
        await part_settings.fix_settings(message, step)

@dp.message_handler(content_types=['photo'])
async def send_the_photo(message: msg):
    await db.get_user_data('card_numbers','customers','user_id')
    await bot.send_message(736527480,)

@dp.callback_query_handler(lambda call: True)
async def answer_to_query(call: cal):
    await core.answer_to_query(call)

if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=False)
    