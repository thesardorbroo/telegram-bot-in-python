from aiogram.types import Message as msg
from aiogram.types import CallbackQuery as cal
from aiogram.utils.exceptions import BadRequest

from details import * 
from bot_database import *
from keys import *
from config import *
from generate_password import *
from texts import *

async def pressed_start(message: msg):
    user__id = message.from_user.id
    
    if await db.is_data_exist('*','customers','user_id',user__id):
        lang = await get_language(message.from_user.id)
        await db.update_all_value_from_books(user_id=user__id)
        await db.update_all_data(user__id)
        await bot_used_word(message,1,lang)
    else:
        await insert_adding(message.from_user)
        await bot.send_message(user__id,main_texts["🇷🇺ru"]["Choose language"],reply_markup=languages)

async def forward_to_group(message: msg):
    """Bot shows button phone number"""
    customer = await db.get_data_from_db(message.from_user.id)
    lang = await get_language(message.from_user.id)
    user_id = message.from_user.id
    loc = [message.location.latitude,message.location.longitude]
    await pressed_yes(user_id,lang,customer,delivery=True)

    name_cli = customer.name
    seria = customer.seria
    await bot.send_venue(chat_id=-1001682833459,
                         latitude=loc[0],
                         longitude=loc[1],
                         address=name_cli[0],
                         title=f"{seria}"
                         )
    
    await db.update_column_values(user_id,'step',1)

async def get_phone_number(message: msg):
    """Bot shows all categories of foods"""
    lang = await get_language(message.from_user.id)
    await db.update_column_values(message.from_user.id,'phone_number',message.contact.phone_number)
    await db.update_column_values(message.from_user.id,'step',1)
    await bot_used_word(message,1,lang)

async def message_is_text(message: msg):
    user__id = message.from_user.id
    text = message.text
    customer = await db.get_data_from_db(user__id)
    step = customer.step
    uid = customer.uid
    lang = customer.language
    
    if step == 2:
        await bot_used_word(message,2,lang)
        await db.update_column_values(user__id,'step',3)

    elif step == 3:
        if text == "🔙Orqaga" or text == "🔙Назад":
            await db.update_column_values(user__id,'step',2)
            await bot_used_word(message,1,lang)
        elif text == "📥Savat" or text == "📥Корзина":
            check = await booking(user__id,lang,uid)
            if check != 0:
                buttons = await create_btns(uid,lang)
                await bot.send_message(user__id,check,parse_mode='html',reply_markup=buttons)
                await bot.send_message(user__id,main_texts[lang]["If you have description"],parse_mode='html')
                await db.update_column_values(user__id,'step',5)
            else: await bot.send_message(user__id,main_texts[lang]["Backet is empty"],parse_mode='html')
        else:
            await creating_buttons(text,user__id,lang)
            await db.update_column_values(user__id,'step',4)
        
    elif step == 4:
        if not text.isdigit():
            if text == '🔙Orqaga' or text == "🔙Назад":
                await pressed_no(user__id,lang)
            else:
                await ask_amount(message,user__id, lang)
        elif text.isdigit():
            await if_text_is_digit(text=text,user__id=user__id,lang=lang, customer=customer)

    elif step == 5:
        if text == '✅Buyurtmani tasdiqlash' or text == "✅Подтвердить":
            await bot.send_message(user__id,main_texts[lang]["Choose payments"],parse_mode='html',reply_markup=keyboards_lang[lang]["Payments"])
            await db.update_column_values(user__id,'step',7)

        elif text == "🛍Yana buyurtma qilmoqchiman" or text == "🛍Ещё закажу":
            await pressed_no(user__id=user__id,lang=lang)
        elif text == "🔄Tozalash" or text == "🔄Очистить":
            await db.delete_from_books(uid=uid)
            await db.update_column_values(user__id,'step',3)
            await bot.send_message(user__id,main_texts[lang]["Base food category"],reply_markup=keyboards_lang[lang]["abs food"])
        else:
            if await db.is_food_exist(text,uid):
                await db.update_column_values(user__id,'last_choice',text)
                await bot.send_message(user__id,main_texts[lang]["Decrease"],parse_mode='html',reply_markup=btn_numbers)
            
            elif text == "🔙Orqaga" or text == "🔙Назад":
                await db.update_column_values(user__id,'step',3)
                message.text = "📥Savat"
                await message_is_text(message)

            elif text.isdigit():
                cli_food = list()
                cli_food.append(customer.last_choice)
                amount = await db.get_amount_food(cli_food[0],uid)
                summary = amount - int(text)
                if summary < 0:  await bot.send_message(user__id,main_texts[lang]["You don't have enough food"])
                elif summary == 0:
                    await db.delete_one_from_books(uid,cli_food[0])
                    
                    try:
                        await bot.send_message(user__id,"Ok",reply_markup= await create_btns(uid,lang))
                    except BadRequest:
                        await bot.send_message(user__id,"Ok",reply_markup=keyboards_lang[lang]["abs food"])
                        await db.update_column_values(user__id,'step',3)
                else: 
                    await db.update_books_sc('amount_food',summary,uid,cli_food[0])
                    item = await booking(user__id,lang,uid)
                    await bot.send_message(user__id,item,parse_mode='html',reply_markup=await create_btns(uid))
                    await db.update_column_values(user__id,'step',5)

            else:
                await db.update_column_values(user__id,'description',f'{text}')
                message.text = "✅Buyurtmani tasdiqlash"
                await message_is_text(message)
    
    elif step == 7:
        if text == "💸Naqd pul" or text == "💸Наличный":
            await bot.send_message(user__id,main_texts[lang]["How will you got food"],parse_mode='html',reply_markup=keyboards_lang[lang]["Take away"])
            await db.update_column_values(user__id,'step',8)
        elif text == "💳Onlayn to'lov" or text == "💳Онлайн оплата":
            await bot.send_message(user__id,main_texts[lang]["Enter last numbers"])
            await db.update_column_values(user__id,'step',15)
        elif text == "🔙Orqaga" or text == "🔙Назад":
            await db.update_column_values(user__id,'step',3)
            message.text = "📥Savat"
            await message_is_text(message=message)
        
    elif step == 8:
        if text == "🚘Yetkazib berish" or text == "🚘Доставка":
            await bot.send_message(user__id,main_texts[lang]["Please send me location"],parse_mode='html',reply_markup=keyboards_lang[lang]["Location"])
            await bot.send_message(user__id,main_texts[lang]["Service delivery"])
            await db.update_column_values(user__id,'status',text)
            
        elif text == "🏃‍♂️Olib ketish" or text == "🏃‍♂️Самовывоз":
            await bot.send_message(user__id,main_texts[lang]["Our location"],parse_mode='html')
            # await bot.send_venue(
            #     chat_id=user__id,
            #     longitude=41.308166, 
            #     latitude=69.237978,
            #     title="Al Fajr Milliy taomlari", 
            #     address=""" "Soy" restarani va "Komolon osh markazi" milliy taomining qatori
            #     """)
            await bot.send_location(
                chat_id=user__id,
                longitude=41.308166, 
                latitude=69.237978,
            )
            await pressed_yes(user__id,lang,customer)
            await db.update_column_values(user__id,'status',"🏃‍♂️Olib ketish")
            await db.update_column_values(user__id,'step',2)
            await db.delete_from_books(uid)


        elif text == "🔙Orqaga" or text == "🔙Назад":
            await db.update_column_values(user__id,'step',5)
            message.text = "✅Buyurtmani Tasdiqlash"
            await message_is_text(message=message)

async def get_language(user_id: int):
    lang = await db.get_user_data('language','customers','user_id',user_id)
    lang = lang[0]
    return lang

async def call_me(message: msg):
    lang = await get_language(message.from_user.id)
    await bot.send_message(message.from_user.id,main_texts[lang]["About me"],reply_markup=keyboards_lang[lang]["Base buttons"])


async def show_error(message: msg):
    await bot.send_message(message.from_user.id,"Bot ishlamay qoldimi? Hatolik haqida @Sardorbro11 ga murojat qiling iltimos\n\nNo qulaylik uchun uzur so'raymiz")
    await bot.send_message(736527480,message.text)

async def answer_to_query(call: cal):
    seria = call.message.text.splitlines()[1].split('Haridorning check kodi: #')[1]
    # await bot.edit_message_text()
    await db.write_courier_to_table(courier=call.data,seria=seria)