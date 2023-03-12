from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def admin_btn():
    btn = InlineKeyboardMarkup(row_width=2)
    btn.add(
        InlineKeyboardButton("✉️ Xabar yolash", callback_data='send'),
    )
    return btn
