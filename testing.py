from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from config import admin_id
from loader import dp, bot
from states import Test
from menu import city, product, first_step, Type_hold

async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text="Бот запущен")


@dp.message_handler(Command("start"), state=None)
async def enter_test(message: types.Message):
    await message.answer("Поздравляем вы подписались на GROOVESTREETBOT 24|7",reply_markup=first_step)

    await Test.Q1.set()

@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(answer1=answer)
    await message.answer("🌆Выберите Ваш город🌆",reply_markup=city)

    await Test.next()
    
@dp.message_handler(state=Test.Q2)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(answer1=answer)
    await message.answer("Выберите товар🛒 \n👇👇👇👇👇👇👇👇👇", reply_markup=product)

    await Test.next()
    
@dp.message_handler(state=Test.Q3)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(answer1=answer)
    await message.answer("Напишите (ГОРОД,РАЙОН, УЛИЦУ, станцию метро).По этим данным БОТ найдет ближайший, актуальный JPS адрес с фото и его описанием. ФОРМА ЗАПОЛНЕНИЯ: Город-Москва, Метро-ВДНХ, Улица-Ленина.")

    await Test.next()
    
@dp.message_handler(state=Test.Q4)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(answer1=answer)
    await message.answer("ВЫБЕРИТЕ ВИД ТАЙНИКА📦 \n👇👇👇👇👇👇👇👇👇",
                         reply_markup=Type_hold)

    await Test.next()


@dp.message_handler(state=Test.Q5)
async def answer_q2(message: types.Message, state: FSMContext):
    #Достаем переменные
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = message.text

    await message.answer("Для получения клада оплатите товар по Киви через любой терминал, либо приложение Qiwi Wallet.\n\nРеквизиты QIWI +79092622993\n\nПосле зачисления средств БОТ ВЫДАСТ АДРЕС В ТЕЧЕНИИ от 30сек до 5мин, Обычно сразу. При затруднении перевода с карты на киви воспользуйтесь этой ссылкой https://qiwi.com/support/")

    # Вариант 1
    await state.finish()


    # Вариант завершения 2 - без стирания данных в data
    # await state.reset_state(with_data=False)
