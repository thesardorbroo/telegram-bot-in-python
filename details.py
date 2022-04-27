from bot_database import *
from generate_password import customer_check
from keys import *
from config import *
from texts import main_texts

# Function insert_adding is perfectly
async def insert_adding(user__id):
    if user__id.first_name != None or user__id.last_name != None:
            fullname = f"{user__id.first_name} {user__id.last_name}"
    else:
        fullname = f"{user__id.username}"
    await db.add_user_into_db(user__id.id,fullname)
    
# Function creating_buttons is perfectly    
async def creating_buttons(text,user__id, lang):
    await bot.send_photo(user__id,open(foods_images[text],"rb"))
    await bot.send_message(user__id,main_texts[lang]["Please choose"],reply_markup=abfoods[text])

# Function booking isn't ready, now!
async def booking(user_id: int, lang, uid,delivery_service = None):
    paper = ""
    summa = 0
    data = await db.check_list(uid)
    if data != 0:
        for i in data:
            txt = f"<b>{i[0]}:\n{i[1]} * {i[2]} = {int(i[2]) * int(i[1])}\n\n</b>"
            paper += txt
            summa += int(i[2]) * int(i[1])
        if delivery_service == None:
            paper += f"""<b>{main_texts[lang]["Summary"]}: {summa}</b>"""
        elif delivery_service == True:
            summa += 10000
            paper += f"""<b>{main_texts[lang]["Service delivery"]}\n{main_texts[lang]["Summary"]}: {summa}</b>"""
        
        return paper
    else: return 0

async def ask_amount(message: Message,user_id, lang):
    try:
        food_cost_name = f"""
        <b>{main_texts[lang]["Name of food"]}: {message.text}\n{main_texts[lang]["Cost of food"]}: {foods[message.text]}</b>"""
        # await message.answer_photo(user_id,open("ovqat.jpeg","rb"),caption=food_cost_name,parse_mode='html')
        # await bot.send_photo(user_id,open("ovqat.jpeg","rb"),caption=food_cost_name,parse_mode='html')   # Har safar boshqa rasm bo'lishi kerak
        await bot.send_message(user_id,food_cost_name,parse_mode='html')
        await bot.send_message(user_id,main_texts[lang]["How many do you need"],parse_mode='html',reply_markup=btn_numbers)
        await db.update_column_values(user_id,'last_choice',message.text)
    except KeyError:
        await bot.send_message(user_id,"Borini tanlang")


async def if_text_is_digit(text,user__id, lang, customer: Customers):
    last_food = customer.last_choice
    
    cost = await db.get_user_data('cost','national_foods','food_name',last_food)
    try:
        await bot.send_message(user__id,
        f"""<b>{last_food}:\n{text} * {cost[0]} = {int(text)*int(cost[0])}\n\n{main_texts[lang]["Do you order something again"]}</b>""",
        parse_mode='html',reply_markup=keyboards_lang[lang]["abs food"])
    except TypeError:
        print("Error expected!")
    await db.update_books(user__id,text,last_food)
    await db.update_column_values(user__id,'step',3)

async def pressed_yes(user_id: int,lang, customer: Customers ,delivery=None):
    description = list()
    uid = customer.uid
    status = customer.status
    description = customer.descrpition
    client = await customer.get_obj_data()
    paper = await booking(user_id,lang,uid,delivery)
    paper_list = paper.splitlines()
    summa = paper_list[len(paper_list) - 1].split(" ")
    summa = summa[1][:-4]
    seria = await customer_check()
    await db.update_column_values(user_id,'seria',seria)
    check_p = await check_paper(client,seria,description,paper,status,lang)
    await bot.send_message(user_id,check_p,reply_markup=keyboards_lang[lang]["Base buttons"],parse_mode='html')
    await bot.send_message(-1001682833459,check_p,reply_markup=delivers,parse_mode='html')
    await bot.send_message(user_id,main_texts[lang]["Say thanks"],reply_markup=keyboards_lang[lang]["Base buttons"])
    await db.update_sales_table(uid,client[2],summa,seria)
    await db.delete_from_books(uid=uid)
    return check_p
    
async def pressed_no(user__id,lang):
    await db.update_column_values(user__id,'step',3)
    await bot.send_message(user__id,main_texts[lang]["Please choose"],reply_markup=keyboards_lang[lang]["abs food"])

async def bot_used_word(message: Message,number: int, lang):
    user_id = message.from_user.id
    try:
        if number == 1:
            await bot.send_message(user_id,main_texts[lang]["Base menu"],reply_markup=keyboards_lang[lang]["Base buttons"])
        elif number == 2:
            await bot.send_message(user_id,main_texts[lang]["Base food category"],reply_markup=keyboards_lang[lang]["abs food"])
    except KeyError:
        info = f"""
User: {message.from_user.first_name}
User id: {message.from_user.id}
User language: {lang}
"""
        await bot.send_message(736527480,info)
        return 0