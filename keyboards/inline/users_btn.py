from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def languages_btn():
    btn = InlineKeyboardMarkup(row_width=2)
    btn.add(
        InlineKeyboardButton('Uz', callback_data='lang:uz'),
        InlineKeyboardButton('Ru', callback_data='lang:ru'),
        InlineKeyboardButton('En', callback_data='lang:en'),
    )
    return btn
