
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from keyboards.default.markups import all_right_message, cancel_message, submit_markup
from aiogram.types import Message
from ..modules.states import SosState
from ..modules.user import IsUser
from ..modules import db
from ..modules import *
from ..import *

@bot.message_handler(commands='sos')
async def cmd_sos(message: Message):
    await SosState.question.set()
    await message.answer('Apa inti permasalahannya? Jelaskan sedetail mungkin dan administrator pasti akan menjawab Anda..', reply_markup=ReplyKeyboardRemove())


@bot.message_handler(state=SosState.question)
async def process_question(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['question'] = message.text

    await message.answer('Memastikan, bahwa semuanya benar.', reply_markup=submit_markup())
    await SosState.next()


@bot.message_handler(lambda message: message.text not in [cancel_message, all_right_message], state=SosState.submit)
async def process_price_invalid(message: Message):
    await message.answer('Tidak ada pilihan seperti itu.')


@bot.message_handler(text=cancel_message, state=SosState.submit)
async def process_cancel(message: Message, state: FSMContext):
    await message.answer('Dibatalkan!', reply_markup=ReplyKeyboardRemove())
    await state.finish()


@bot.message_handler(text=all_right_message, state=SosState.submit)
async def process_submit(message: Message, state: FSMContext):

    cid = message.chat.id

    if db.fetchone('SELECT * FROM questions WHERE cid=?', (cid,)) == None:

        async with state.proxy() as data:
            db.query('INSERT INTO questions VALUES (?, ?)',
                     (cid, data['question']))

        await message.answer('Terkirim!', reply_markup=ReplyKeyboardRemove())

    else:

        await message.answer('Batas jumlah pertanyaan yang diajukan telah terlampaui.', reply_markup=ReplyKeyboardRemove())

    await state.finish()
