from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="O'zbekcha"), KeyboardButton(text="Русский"),KeyboardButton(text="English"))
    return rkm


def ozb_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="🛍 Buyurtma berish"))
    rkm.row(KeyboardButton(text="🎉 Aksiya"), KeyboardButton(text="🏘 Barcha filiallar"))
    rkm.row(KeyboardButton(text="📋 Mening buyurtmalarim"), KeyboardButton(text="✍️Izoh qoldirish"))
    rkm.row(KeyboardButton(text="💼 Vakansiyalar"), KeyboardButton(text="ℹ️ Biz haqimizda"))
    rkm.row(KeyboardButton(text="⚙️ Sozlamalar"))
    return rkm

def buyurt_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="🚖 Yetkazib berish"),KeyboardButton(text="🏃 Olib ketish"))
    rkm.row(KeyboardButton(text="⬅️ Orqaga"))
    return rkm

def orqaga_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="⬅️ Orqaga"))
    return rkm

def sozlamalar_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="🇺🇿 Tilni o'zgartirish"),KeyboardButton(text="Tug'ilgan kunni qo'shish"))
    rkm.row(KeyboardButton(text="Telefon raqamni o'zgartirish"),KeyboardButton(text="⬅️ Orqaga"))
    return rkm

def barcha_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="⬅️ Orqaga"),KeyboardButton(text="▶️ Oldinga"))
    rkm.row(KeyboardButton(text="MAX WAY BERUNIY"),KeyboardButton(text="MAX WAY ATLAS"))
    rkm.row(KeyboardButton(text="MAX WAY - DRUJBA"),KeyboardButton(text="MAX WAY MEGA PLANET"))
    rkm.row(KeyboardButton(text="MAX WAY AVIASOZLAR"),KeyboardButton(text="MAX WAY RISOVIY"))
    rkm.row(KeyboardButton(text="MAX WAY PARUS"),KeyboardButton(text="MAX WAY MAGIC CITY"))
    rkm.row(KeyboardButton(text="MAX WAY SAMARQAND DARVOZA"),KeyboardButton(text="MAX WAY PARKENT"))
    return rkm