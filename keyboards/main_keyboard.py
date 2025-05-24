from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Добавить фото", callback_data="add_photo"),
     InlineKeyboardButton(text="Удалить фото", callback_data="delete_photo")],
    [InlineKeyboardButton(text="Вернуться назад", callback_data="back_home")],
    [InlineKeyboardButton(text="Посмотреть бд", callback_data="open_bd")]
])

add_photo_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Вернуться назад", callback_data="back_home")],
])
