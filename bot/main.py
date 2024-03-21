# Aiogram
import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Command
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder

#Files
import config as cfg
import keyboard as kb
from db import Database

bot = Bot(token=cfg.TOKEN)
dp = Dispatcher()
db = Database('database.db')

# render_html.py
def render_html_page(user_data=None):
    return render_template('index.html', user_data=user_data)

# --------------- CALLBACKS ---------------

# --- start ---

@dp.message(Command('start'))
async def cmd_start(message: Message):
    user_id = message.from_user.id
    
    if not db.user_exists(message.from_user.id):
        start_command = message.text
        referrer_id = str(start_command[7:])
        if str(referrer_id) != "":
            if str(referrer_id) != str(message.from_user.id):
                db.add_user(message.from_user.id, referrer_id)
                try:
                    await bot.send_message(referrer_id, "По вашей реферальной ссылке зарегистрировались!")
                except:
                    pass
            else:
                db.add_user(message.from_user.id)
                await bot.send_message("Нельзя регистрировать по собственной реферальной ссылке!")
        else:
            db.add_user(message.from_user.id)
        
        user_data = db.get_user_data(user_id)
        await bot.send_response(message.chat.id, content_type='html', data=render_html_page(user_data))
        
        await message.answer("Welcome message", parse_mode='Markdown', reply_markup = kb.main_menu)
    else:        
        await message.answer("Welcome message", parse_mode='Markdown', reply_markup = kb.main_menu)
        
# --- how to play ---
@dp.callback_query(F.data == 'how_to_play')
async def how_to_play(callback: CallbackQuery):
    await bot.edit_message_text('Random message', chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=kb.back_to_menu)

# --- profile stats ---
@dp.callback_query(F.data == 'stats')
async def profile_stats(callback: CallbackQuery):
    await bot.edit_message_text('Random message', chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=kb.show_profile_stats)

@dp.callback_query(F.data == 'invite_friend')
async def invite_friend(callback: CallbackQuery):
    await bot.edit_message_text(f'Your refferal link:\n\nhttps://t.me/{cfg.BOT_NICKNAME}?start={callback.from_user.id}\n\nRefferals: 0', chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=kb.back_to_menu)

@dp.callback_query(F.data == 'back_to_menu')
async def back_to_menu(callback: CallbackQuery):
    await bot.edit_message_text('Welcome message', chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=kb.main_menu)

# --------------- CALLBACKS ---------------

# --------------- START FUNCTION ---------------
async def main():
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    asyncio.run(main())
# --------------- START FUNCTION ---------------

