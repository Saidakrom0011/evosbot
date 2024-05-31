from aiogram import Bot,Dispatcher,executor,types
from aiogram.dispatcher.filters import Text

from ky import main_menu,ozb_menu,buyurt_menu,orqaga_menu,sozlamalar_menu,barcha_menu

BOT_TOKEN= "7056676353:AAEYcBXSS5kQsWa5B6Amch64cf0S5-gjvOI"

bot =  Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)
photo_max_way="https://resto.uz/data/resto/45/4482/max-way-3253.png"
photo_m="https://cdn.delever.uz/delever/c548b8fc-3f0d-4180-ad2d-b0419c040101"
@dp.message_handler(commands="start")
async def start_bot(message : types.Message):
    await message.answer("""Buyurtma berishni boshlash uchun 🛍 Buyurtma berish tugmasini bosing
 
Shuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin

<a href='https://maxway.uz/uz'>Menu</a>""",
                         parse_mode="HTML",
                         reply_markup=main_menu())


@dp.message_handler(Text(equals="O'zbekcha"))
async def start_bot(message: types.Message):
    await message.answer("""Buyurtma berishni boshlash uchun 🛍 Buyurtma berish tugmasini bosing

Shuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin

<a href='https://maxway.uz/uz'>Menu</a>""",
                         parse_mode="HTML",
                         reply_markup=ozb_menu())

@dp.message_handler(Text(equals="🛍 Buyurtma berish"))
async def start_bot(message: types.Message):
    await message.answer("Yetkazib berish turini tanlang",
                         reply_markup=buyurt_menu())

@dp.message_handler(Text(equals="⬅️ Orqaga"))
async def start_bot(message: types.Message):
    await message.answer("""Buyurtma berishni boshlash uchun 🛍 Buyurtma berish tugmasini bosing

Shuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin

<a href='https://maxway.uz/uz'>Menu</a>""",
                         parse_mode="HTML",
                         reply_markup=ozb_menu())

@dp.message_handler(Text(equals="🎉 Aksiya"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo_m,caption="""BEPUL YETKAZIB BERAMIZ 🚚 
 3ta Maxi Box yoki ko’proq buyurtma qiling va bepul yetkazib berish xizmatiga ega bo’ling!😋""",reply_markup=orqaga_menu())


@dp.message_handler(Text(equals="📋 Mening buyurtmalarim"))
async def start_bot(message: types.Message):
    await message.answer(text="""Sizda buyurtmalar yo'q""",reply_markup=orqaga_menu())

@dp.message_handler(Text(equals="✍️Izoh qoldirish"))
async def start_bot(message: types.Message):
    await message.answer(text="""Izoh qoldiring. Sizning fikringiz biz uchun muhim""",reply_markup=orqaga_menu())

@dp.message_handler(Text(equals="ℹ️ Biz haqimizda"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo_max_way,caption="""🍟 Max Way 
☎️ Aloqa markazi: +998712005400""",reply_markup=orqaga_menu())

@dp.message_handler(Text(equals="⚙️ Sozlamalar"))
async def start_bot(message: types.Message):
    await message.answer(text="""Izoh qoldiring. Sizning fikringiz biz uchun muhim""",reply_markup=sozlamalar_menu())

@dp.message_handler(Text(equals="🇺🇿 Tilni o'zgartirish"))
async def start_bot(message: types.Message):
    await message.answer(text="""O'zgartirmoqchi bo'lgan tilingizni tanlang""",reply_markup=main_menu())


#+==================================================

@dp.message_handler(Text(equals="🏘 Barcha filiallar"))
async def start_bot(message: types.Message):
    await message.answer(text="""Bizning filiallarimiz :""",reply_markup=barcha_menu())


@dp.message_handler(Text(equals="MAX WAY BERUNIY"))
async def orqa_bot(message: types.Message):
    await message.answer(text="""📍 Filial:  MAX WAY BERUNIY 
                     
🗺 Manzil:  улица Беруни, 47, Ташкент 
                     
🏢 Orientir:  Метро Беруний 
                     
☎️ Telefon raqami:  +998712005400
                     
🕙 Ish vaqti : 10:00 - 22:00""")
    latitude = 41.342807
    longitude = 69.264684
    await message.answer_location(latitude=latitude, longitude=longitude)


@dp.message_handler(Text(equals="MAX WAY ATLAS"))
async def orqa_bot(message: types.Message):
    await message.answer(text="""📍 Filial:  MAX WAY ATLAS 
                     
🗺 Manzil:  улица Катартал, 28, Ташкент 
                     
🏢 Orientir:  CHILONZOR ATLAS 
                     
☎️ Telefon raqami:  +998712005400
                     
🕙 Ish vaqti : 10:00 - 22:00""")
    latitude = 41.342807
    longitude = 69.264684
    await message.answer_location(latitude=latitude, longitude=longitude)

@dp.message_handler(Text(equals="MAX WAY - DRUJBA"))
async def orqa_bot(message: types.Message):
    await message.answer(text="""📍 Filial:  MAX WAY - DRUJBA 
                     
🗺 Manzil:  микрорайон Алмазар, 8/2, Чиланзарский район, Ташкент 
                     
🏢 Orientir:  Метро Xalqlar do'stligi 
                     
☎️ Telefon raqami:  +998712005400
                     
🕙 Ish vaqti : 10:00 - 04:00""")
    latitude = 41.342807
    longitude = 69.264684
    await message.answer_location(latitude=latitude, longitude=longitude)


@dp.message_handler(Text(equals="MAX WAY MEGA PLANET"))
async def orqa_bot(message: types.Message):
    await message.answer(text="""📍 Filial:  MAX WAY MEGA PLANET 
                     
🗺 Manzil:  улица Ниязбек, 1 
                     
🏢 Orientir:  улица Ниязбек, 1 
                     
☎️ Telefon raqami:  +998712005400
                     
🕙 Ish vaqti : 10:00 - 03:00""")
    latitude = 41.342807
    longitude = 69.264684
    await message.answer_location(latitude=latitude, longitude=longitude)


@dp.message_handler(Text(equals="MAX WAY AVIASOZLAR"))
async def orqa_bot(message: types.Message):
    await message.answer(text="""📍 Filial:  MAX WAY AVIASOZLAR 
                     
🗺 Manzil:  улица Авиасозлар, 23 
                     
🏢 Orientir:   
                     
☎️ Telefon raqami:  +998712005400
                     
🕙 Ish vaqti : 10:00 - 03:00""")
    latitude = 41.342807
    longitude = 69.264684
    await message.answer_location(latitude=latitude, longitude=longitude)


@dp.message_handler(Text(equals="MAX WAY RISOVIY"))
async def orqa_bot(message: types.Message):
    await message.answer(text="""📍 Filial:  MAX WAY RISOVIY 
                     
🗺 Manzil:  Узбекистан, Ташкент, Алтынкульская улица, 10 
                     
🏢 Orientir:  банкетный зал Тантана 
                     
☎️ Telefon raqami:  +998712005400
                     
🕙 Ish vaqti : 10:00 - 03:00""")
    latitude = 41.342807
    longitude = 69.264684
    await message.answer_location(latitude=latitude, longitude=longitude)


@dp.message_handler(Text(equals="MAX WAY PARUS"))
async def orqa_bot(message: types.Message):
    await message.answer(text="""📍 Filial:  MAX WAY PARUS 
                     
🗺 Manzil:  улица Катартал, 60/5 
                     
🏢 Orientir:  ТЦ Парус 
                     
☎️ Telefon raqami:  +998712005400
                     
🕙 Ish vaqti : 10:00 - 03:00""")
    latitude = 41.342807
    longitude = 69.264684
    await message.answer_location(latitude=latitude, longitude=longitude)



@dp.message_handler(Text(equals="MAX WAY MAGIC CITY"))
async def orqa_bot(message: types.Message):
    await message.answer(text="""📍 Filial:  MAX WAY MAGIC CITY 
                     
🗺 Manzil:  Узбекистан, Ташкент, улица Бабура, 174/6 
                     
🏢 Orientir:  Magic City 
                     
☎️ Telefon raqami:  +998712005400
                     
🕙 Ish vaqti : 10:00 - 22:00""")
    latitude = 41.342807
    longitude = 69.264684
    await message.answer_location(latitude=latitude, longitude=longitude)

@dp.message_handler(Text(equals="MAX WAY SAMARQAND DARVOZA"))
async def orqa_bot(message: types.Message):
    await message.answer(text="""📍 Filial:  MAX WAY SAMARQAND DARVOZA 
                     
🗺 Manzil:  Узбекистан, Ташкент, улица Коратош, 5А 
                     
🏢 Orientir:  Samarqand Darvoza 
                     
☎️ Telefon raqami:  +998712005400
                     
🕙 Ish vaqti : 10:00 - 22:00""")
    latitude = 41.342807
    longitude = 69.264684
    await message.answer_location(latitude=latitude, longitude=longitude)

@dp.message_handler(Text(equals="MAX WAY PARKENT"))
async def orqa_bot(message: types.Message):
    await message.answer(text="""📍 Filial:  MAX WAY PARKENT 
                     
🗺 Manzil:  Узбекистан, Ташкент, Яшнободский район, массив Мавлоно Риёзи, 30В 
                     
🏢 Orientir:  Паркентский рынок 
                     
☎️ Telefon raqami:  +998712005400
                     
🕙 Ish vaqti : 10:00 - 03:00""")
    latitude = 41.342807
    longitude = 69.264684
    await message.answer_location(latitude=latitude, longitude=longitude)



@dp.message_handler(Text(equals="💼 Vakansiyalar"))
async def start_bot(message: types.Message):
    await message.answer(text="""O'zgartirmoqchi bo'lgan tilingizni tanlang""",reply_markup=main_menu())


if __name__ == '__main__':
    executor.start_polling(dp)