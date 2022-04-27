from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
from config import db

languages = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2).add(
    KeyboardButton('🇺🇿uz'),KeyboardButton('🇷🇺ru')
)

language_to_change = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2).add(
    KeyboardButton("uz🇺🇿"),KeyboardButton("ru🇷🇺")
)

one_step_back = KeyboardButton('🔙Orqaga')
one_step_back_ru = KeyboardButton("🔙Назад")

btn_location = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=False).add(
    KeyboardButton("Lokatsiya jo'natish 📍",request_location=True)
)

btn_location_ru = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=False).add(
    KeyboardButton("Отправить геолокацию 📍",request_location=True)
)
pnumber_ru = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=False).add(
    KeyboardButton("Оправить номер телефон 📱",request_contact=True)
)

pnumber = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=False).add(
    KeyboardButton("Telefon raqamni jo'natish 📱",request_contact=True)
)
payments_ru = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2).add(
    KeyboardButton("💸Наличный"),
    KeyboardButton("💳Онлайн оплата"),
    one_step_back_ru
)

payments = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2).add(
    KeyboardButton("💸Naqd pul"),
    KeyboardButton("💳Onlayn to'lov"),
    one_step_back
)

take_away_or_to_deliver_ru = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2).add(
    KeyboardButton("🚘Доставка"),
    KeyboardButton("🏃‍♂️Самовывоз"),
    one_step_back_ru
)

take_away_or_to_deliver = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2).add(
    KeyboardButton("🚘Yetkazib berish"),
    KeyboardButton("🏃‍♂️Olib ketish"),
    one_step_back
)
base_buttons = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2).add(
    KeyboardButton("🛍Buyurtma berish"),
    KeyboardButton("⚙️Sozlamalar"),     
    KeyboardButton("📞Biz bilan aloqa")
)
base_buttons_ru = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2).add(
    KeyboardButton("🛍Заказать"),
    KeyboardButton("⚙️Настойка"),     
    KeyboardButton("📞Связаться с нами")
)

abs_foods_ru = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2).add(
    one_step_back_ru,
    KeyboardButton('📥Корзина'),
    KeyboardButton("🍹Воды"), # 🍲🥙
    KeyboardButton("🥗Салаты"),
    KeyboardButton("🧆Узбекская кухня"),
    KeyboardButton("🍜Первый блюда"), 
    KeyboardButton("🍛Уйгурская кухня"),
    KeyboardButton("🥘Мангал"),
    KeyboardButton("🍢Шашлыки"),
    KeyboardButton("🍢Кавказский шашлыки"),
)

abs_foods = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2).add(
    KeyboardButton('🔙Orqaga'),
    KeyboardButton('📥Savat'),
    KeyboardButton("🍹Ichimliklar"), # 🍲🥙
    KeyboardButton("🥗Salatlar"),
    KeyboardButton("🧆Milliy taomlar"),
    KeyboardButton("🍜Suyuq taomlar"),
    KeyboardButton("🍛Uygur taomlar"),
    KeyboardButton("🥘Mangal"),
    KeyboardButton("🍢Kaboblar"),
    KeyboardButton("🍢Kavkaz kaboblar"),
)
ichimliklar = ReplyKeyboardMarkup(resize_keyboard=True,row_width=3).add(
    KeyboardButton('Pepsi 0.5'),
    KeyboardButton('Pepsi 1'),
    KeyboardButton('Pepsi 1.5'),
    KeyboardButton('Coca Cola 0.5'),
    KeyboardButton('Coca Cola 1'),
    KeyboardButton('Coca Cola 1.5'),
    KeyboardButton('Mineral suv 0.5'),
    KeyboardButton('Mineral suv 1'),
    KeyboardButton('Mineral suv 1.5'),
    KeyboardButton('Sharbat'),
    KeyboardButton('Kampot kichkina'),
    KeyboardButton('Kampot katta'),
    KeyboardButton('Coffee'),
    KeyboardButton('Limon choy'),
    KeyboardButton('Oddiy choy'),
    KeyboardButton('Non kichkina'),
    KeyboardButton('Non katta'),
    one_step_back
)
btn_numbers = ReplyKeyboardMarkup(resize_keyboard=True,row_width=3).add(
    KeyboardButton('1'),
    KeyboardButton('2'),
    KeyboardButton('3'),
    KeyboardButton('4'),
    KeyboardButton('5'),
    KeyboardButton('6'),
    KeyboardButton('7'),
    KeyboardButton('8'),
    KeyboardButton('9'),
    KeyboardButton('0'),
    one_step_back
)
salatlar = ReplyKeyboardMarkup(resize_keyboard=True,row_width=3).add(
    KeyboardButton('Мужской каприз'),KeyboardButton('Под шуба'),
    KeyboardButton('Мафтункор'),KeyboardButton('Мясное ассорти'),
    KeyboardButton('Свежий ассорти'),KeyboardButton('Сузма'),
    KeyboardButton('Тузлама(кичкина)'),KeyboardButton('Тузлама(катта)'),KeyboardButton('Катикли салат'),
    KeyboardButton('Аччик-чучук'),KeyboardButton('Холодец'),
    KeyboardButton('Катик'),KeyboardButton('Алфажр салат'),
    KeyboardButton('Греческий'),KeyboardButton('Смак'),
    KeyboardButton('Крабовый'),KeyboardButton('Диета'),
    KeyboardButton('Истанбул'),KeyboardButton('Анкара'),
    KeyboardButton('Японский'),KeyboardButton('Гнездо глухаря'),
    KeyboardButton('Ажабсанда'),KeyboardButton('Дамский каприз'),
    KeyboardButton('Греческая лоза'),KeyboardButton('Турп салат'),
    KeyboardButton('Тошкент'),KeyboardButton('Американский'),
    KeyboardButton('Оливье'),KeyboardButton('Цезарь'),
    one_step_back
)
mangal = ReplyKeyboardMarkup(resize_keyboard=True,row_width=3).add(
    KeyboardButton('Бон филе(1кг)'),KeyboardButton('Рибай стейк(1кг)'),
    KeyboardButton('Баранья корейка(1кг)'),KeyboardButton('Тибон стейк(1кг)'),
    KeyboardButton('Сосиски(1шт)'),KeyboardButton('Рыба(1кг)'),
    KeyboardButton('Овощи на мангале(1кг)'),KeyboardButton('Котлет(1шт)'),
    KeyboardButton('Кукуруза(1шт)'),KeyboardButton('Куриные грудинка(1кг)'),
    KeyboardButton('Куриные крылышки(1кг)'),KeyboardButton('Бедана'),
    KeyboardButton('Куриное бедро(1шт)'),KeyboardButton('Бутун товук(1шт)'),
    one_step_back
)

kaboblar = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2).add(
    KeyboardButton('Жаз (куй гушти)'),KeyboardButton('Жаз (мол гушти)'),
    KeyboardButton('Кийма'),KeyboardButton('Кийма (товукли)'),
    KeyboardButton('Товук'),KeyboardButton('Жигар'),
    KeyboardButton('Жигар рулет'),KeyboardButton('Куй (ср)'),
    KeyboardButton('Мол (ср)'),KeyboardButton('Кийма (ср)'),
    one_step_back
)

kavkaz_kaboblar = ReplyKeyboardMarkup(resize_keyboard=True,row_width=3).add(
    KeyboardButton('Корейка'),KeyboardButton('Куй (кусковой)'),
    KeyboardButton('Мол (кусковой)'),KeyboardButton('Урдак'),
    KeyboardButton('Балик'),KeyboardButton('Товук бедро'),
    KeyboardButton('Товук канот'),KeyboardButton('Кийма (кавказча)'),
    KeyboardButton('Кийма (пишлок билан кукат)'),KeyboardButton('Кийма (товукли кавказча)'),
    KeyboardButton('Кийма (пишлок билан товук)'),KeyboardButton('Кузикорин (Грибы)'),
    KeyboardButton('Овощной'),KeyboardButton('Картошка (думба билан)'),
    KeyboardButton('Кийма (картошкали)'),one_step_back
)

uygur_taomlar = ReplyKeyboardMarkup(resize_keyboard=True,row_width=3).add(
    KeyboardButton('Манти'),KeyboardButton('Манти (сувли)'),
    KeyboardButton('Кефси(кичкина)'),KeyboardButton('Кефси(катта)'),
    KeyboardButton('Сокоро(кичкина)'),KeyboardButton('Сокоро(катта)'),
    KeyboardButton('Сумборо(кичкина)'),KeyboardButton('Сумборо(катта)'),
    KeyboardButton('Лазеру (аччик гушт)(кичкина)'),KeyboardButton('Лазеру (аччик гушт)(катта)'),
    KeyboardButton('Мушуру (тухумсай + грибы)'),KeyboardButton('Думсай'),
    KeyboardButton('Тухумсай(кичкина)'),KeyboardButton('Тухумсай(катта)'),
    KeyboardButton('Айримсай'),KeyboardButton('Ковурма лагмон(кичкина)'),KeyboardButton('Ковурма лагмон(катта)'),
    KeyboardButton('Лагман(кичкина)'),KeyboardButton('Лагман(катта)'),KeyboardButton('Босо'),
    KeyboardButton('Гушт сай(кичкина)'),KeyboardButton('Гушт сай(катта)'),
    KeyboardButton('Ганпан(кичкина)'),KeyboardButton('Ганпан(катта)'),
    KeyboardButton('Товук сай'),one_step_back
)
milliy_taomlar = ReplyKeyboardMarkup(resize_keyboard=True,row_width=3).add(
    KeyboardButton('Табака'),KeyboardButton('Ош(кичкина)'),KeyboardButton('Ош(катта)'),
    KeyboardButton('Нохот-шурак'),KeyboardButton('Бешбармок(кичкина)'),KeyboardButton('Бешбармок(катта)'),
    KeyboardButton('Халим'),KeyboardButton('Козон-кабоб'),
    KeyboardButton('Ассорти'),KeyboardButton('Баранья ножка'),
    KeyboardButton('Норин'),KeyboardButton('Бифштекс'),
    KeyboardButton('Бефстроган'),KeyboardButton('Тушенка'),
    KeyboardButton('Дулма'),KeyboardButton('Куза тушенка'),
    KeyboardButton('Сомса'),KeyboardButton('Чучвара домашний'),
    KeyboardButton('Товукли казон-кабоб'),KeyboardButton('Думгаза'),
    KeyboardButton('Балик (сазан)'),KeyboardButton('Балик (судак)(кичкина)'),KeyboardButton('Балик (судак)(катта)'),
    one_step_back
)
suyuq_taomlar = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2).add(
    KeyboardButton('Манпар'),KeyboardButton('Мастава'),
    KeyboardButton('Шурва'),KeyboardButton('Мошхурда'),
    KeyboardButton('Окрошка'),KeyboardButton('Кукси'),
    KeyboardButton('Куз шурва'),KeyboardButton('Фрикадельки'),
    KeyboardButton('Куриная лапша'),KeyboardButton('Чучвара'),
    KeyboardButton('Хаш'),one_step_back
)
delivers = InlineKeyboardMarkup(resize=True,row_width=2).add(
    InlineKeyboardButton('Davron',callback_data='Davron')
)

change_number = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2).add(
    KeyboardButton("Tilni o'zgartirish 🇺🇿"),KeyboardButton("Telefon raqam 📱"),
    one_step_back  
)

change_number_ru = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2).add(
    KeyboardButton("Изменить язык 🇷🇺"),KeyboardButton("Телефон номер 📱"),
    one_step_back_ru  
)

abfoods = {
    "🍹Ichimliklar": ichimliklar,
    "🥗Salatlar": salatlar,
    "🧆Milliy taomlar": milliy_taomlar,
    "🍜Suyuq taomlar": suyuq_taomlar,
    "🍛Uygur taomlar": uygur_taomlar,
    "🥘Mangal": mangal,
    "🍢Kaboblar":kaboblar,
    "🍢Kavkaz kaboblar":kavkaz_kaboblar,
    "🍹Воды": ichimliklar,
    "🥗Салаты": salatlar,
    "🧆Узбекская кухня": milliy_taomlar,
    "🍜Первый блюда": suyuq_taomlar,
    "🍛Уйгурская кухня": uygur_taomlar,
    "🥘Мангал": mangal,
    "🍢Шашлыки":kaboblar,
    "🍢Кавказский шашлыки":kavkaz_kaboblar,
}

keyboards_lang = {
    "🇷🇺ru":{
        "Phone number": pnumber_ru,
        "Location": btn_location_ru,
        "Payments": payments_ru,
        "Take away": take_away_or_to_deliver_ru,
        "Base buttons": base_buttons_ru,
        "abs food": abs_foods_ru,
        "change": change_number_ru,
    },
    "🇺🇿uz":{
        "Phone number": pnumber,
        "Location": btn_location,
        "Payments": payments,
        "Take away": take_away_or_to_deliver,
        "Base buttons": base_buttons,
        "abs food": abs_foods,
        "change": change_number,
    },
}






async def check_paper(client: list, seria: str, description: str, paper: str, status: str,lang):
    if lang == "🇺🇿uz":      # 🇷🇺ru 🇺🇿uz
        cl = "Haridorning"
        check_paper = f"""
<b>Haridor tanlovi:</b> {status}
<b>{cl} id raqami:</b> {client[1]}
<b>{cl} check kodi:</b> #{seria}
<b>{cl} ismi:</b> {client[2]}
<b>{cl} telefon raqami:</b> {client[3]}
<b>Qo'shimcha ma'lumot:</b> {description}
<b>{cl} buyurtmasi:</b>\n{paper}
    """
    else:
        cl = "Клиент"
        check_paper = f"""
<b>Выбор клиент:</b> {status}
<b>{cl} телеграм айди:</b> {client[1]}
<b>{cl} чек серия:</b> #{seria}
<b>{cl} имя:</b> {client[2]}
<b>{cl} номер телефона:</b> {client[3]}
<b>Допалнительные информации:</b> {description}
<b>{cl} заказ:</b>\n{paper}
    """
    return check_paper

async def create_btns(uid: int,lang):
    foods = await db.m_to_create_btns(uid)
    try:
        btns = ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
        for i in foods:
                btns.add(KeyboardButton(i[0]))
        if lang == "🇺🇿uz":
            btns.add(KeyboardButton("🔄Tozalash"),KeyboardButton('✅Buyurtmani tasdiqlash'),KeyboardButton("🛍Yana buyurtma qilmoqchiman"))
        else:
            btns.add(KeyboardButton("🔄Очистить"),KeyboardButton('✅Подтвердить'),KeyboardButton("🛍Ещё закажу"))
        return btns
    except TypeError:
        return 0

