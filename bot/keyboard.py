from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.types.web_app_info import WebAppInfo

main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="💎 Let's play", web_app=WebAppInfo(url='https://kinstering.github.io/TabletWebApp/', isExpanded=True))],
    [InlineKeyboardButton(text="❓ How to play?", callback_data='how_to_play'),
     InlineKeyboardButton(text="📊 Show my profile stats", callback_data='stats')]
])

asralium_comminity = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="👨‍💻 Astralium community", url=''),
    InlineKeyboardButton(text="📱 Astralium on X", url='')],
    [InlineKeyboardButton(text="💎 Play", web_app=WebAppInfo(url='https://kinstering.github.io/TabletWebApp/', isExpanded=True))],
])

asralium_comminity = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="💎 Play", web_app=WebAppInfo(url='https://kinstering.github.io/TabletWebApp/', isExpanded=True))]
])

show_profile_stats = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="💎 Play", web_app=WebAppInfo(url='https://kinstering.github.io/TabletWebApp/', isExpanded=True)),
     InlineKeyboardButton(text="👬 Invite friend", callback_data='invite_friend')],
    [InlineKeyboardButton(text="◀️ Back to menu", callback_data='back_to_menu')]
])

back_to_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="◀️ Back to menu", callback_data='back_to_menu')]
])