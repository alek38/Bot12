from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

first_step = ReplyKeyboardMarkup(
    keyboard=[
    [
    KeyboardButton(text="👉👉!!!ЖМИ СЮДА!!!👈👈"),
    ],
     ],
    resize_keyboard=True,one_time_keyboard=True
)

city = ReplyKeyboardMarkup(
    keyboard=[
    [KeyboardButton(text="Москва")],
    [KeyboardButton(text="Санкт-Петербург")],
    [KeyboardButton(text="Новосибирск")],
    [KeyboardButton(text="Екатеринбург")],
    [KeyboardButton(text="Казань")],
    [KeyboardButton(text="Самара")],
    [KeyboardButton(text="Омск")],
    [KeyboardButton(text="Ростов-на-Дону")],
    [KeyboardButton(text="Уфа")],
    [KeyboardButton(text="Красноярск")],
    [KeyboardButton(text="Воронеж")],
    [KeyboardButton(text="Нижний Новгород")],
    [KeyboardButton(text="Пермь")],
    [KeyboardButton(text="Волгоград")],
    [KeyboardButton(text="Краснодар")],
    [KeyboardButton(text="Саратов")],
    [KeyboardButton(text="Тюмень")],
    [KeyboardButton(text="Тольятти")],
    [KeyboardButton(text="Челябинск"),],
     ],
    resize_keyboard=True, one_time_keyboard=True
)
product = ReplyKeyboardMarkup(
    keyboard=[
    [KeyboardButton(text="Шишки Белая вдова - 1300р за 1гр")],
    [KeyboardButton(text="Гашиш Diamond Haze - 1000р за 1гр")],
    [KeyboardButton(text="Амфетамин S4 - 1300р за 1гр")],
    [KeyboardButton(text="Кокаин - 8500р за 1гр")],
    [KeyboardButton(text="MDMA - 3000р за 1гр")],
    [KeyboardButton(text="Мефедрон - 1500р")],
     ],
    resize_keyboard=True, one_time_keyboard=True
)
Type_hold = ReplyKeyboardMarkup(
    keyboard=[
    [KeyboardButton(text="Клад(лес🌳) кол-во 3")],
    [KeyboardButton(text="Клад(город🏙 ) кол-во 1")],
    [KeyboardButton(text="Магнит(город🌆)кол-во 1")],
     ],
    resize_keyboard=True, one_time_keyboard=True
)
Deсision = ReplyKeyboardMarkup(
    keyboard=[
    [
    KeyboardButton(text="ДА"),
    KeyboardButton(text="НЕТ"),
    ],
     ],
    resize_keyboard=True, one_time_keyboard=True
)
