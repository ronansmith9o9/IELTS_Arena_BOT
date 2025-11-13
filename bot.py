import telebot
from telebot import types
from handlers.main_menu import get_main_menu
from handlers.reading import register_reading_handlers
from handlers.listening import register_listening_handlers
from handlers.writing import register_writing_handlers
from handlers.speaking import register_speaking_handler  # <-- speaking.py dan

TOKEN = "8276217068:AAESR-xxhwcFaMf6zXIwQynlm3CN7LNiAFI"
CHANNEL = "@American_Life018"  # Kanal username

bot = telebot.TeleBot(TOKEN)

# --- foydalanuvchi holati saqlanadi ---
user_data = {}   # {user_id: {'first_name':..., 'last_name':..., 'phone':...}}
user_state = {}  # {user_id: 'waiting_name' / 'waiting_family' / 'waiting_phone'}

# --- Kanalga obuna tekshirish ---
def is_subscribed(user_id):
    try:
        status = bot.get_chat_member(CHANNEL, user_id).status
        return status in ['member', 'creator', 'administrator']
    except:
        return False

# --- Start komandasi ---
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id

    # Kanalga obuna sharti
    if not is_subscribed(user_id):
        markup = types.InlineKeyboardMarkup()
        subscribe_btn = types.InlineKeyboardButton("Obuna bo‘lish", url=f"https://t.me/{CHANNEL[1:]}")
        confirm_btn = types.InlineKeyboardButton("Tasdiqlash ✅", callback_data="confirm_sub")
        markup.add(subscribe_btn)
        markup.add(confirm_btn)
        bot.send_message(message.chat.id,
                         "Botni ishlatish uchun kanalga obuna bo‘ling va tasdiqlang 👇",
                         reply_markup=markup)
        return

    # Agar foydalanuvchi hali ma’lumot kiritmagan bo‘lsa
    if user_id not in user_data:
        bot.send_message(message.chat.id, "Iltimos, ismingizni kiriting:")
        user_state[user_id] = 'waiting_name'
        return

    # Aks holda asosiy menyu
    bot.send_message(message.chat.id, "Xush kelibsiz!", reply_markup=get_main_menu())

# --- Callback tugmalar ---
@bot.callback_query_handler(func=lambda call: call.data == "confirm_sub")
def confirm_subscription(call):
    user_id = call.from_user.id
    if is_subscribed(user_id):
        bot.answer_callback_query(call.id, "Obuna tasdiqlandi ✅")

        # Callback xabarni o‘chirish
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except:
            pass

        if user_id not in user_data:
            bot.send_message(call.message.chat.id, "Iltimos, ismingizni kiriting:")
            user_state[user_id] = 'waiting_name'
        else:
            bot.send_message(call.message.chat.id, "Xush kelibsiz!", reply_markup=get_main_menu())
    else:
        bot.answer_callback_query(call.id, "Siz hali kanalga obuna bo‘lmadingiz ❌")
        bot.send_message(call.message.chat.id, "Iltimos, kanalga obuna bo‘ling va keyin tasdiqlang.")

# --- Foydalanuvchi ma’lumotlarini qabul qilish ---
@bot.message_handler(func=lambda m: user_state.get(m.from_user.id) is not None)
def handle_user_info(message):
    user_id = message.from_user.id
    state = user_state.get(user_id)

    if state == 'waiting_name':
        user_data[user_id] = {'first_name': message.text}
        user_state[user_id] = 'waiting_family'
        bot.send_message(message.chat.id, "Familyangizni kiriting:")

    elif state == 'waiting_family':
        user_data[user_id]['last_name'] = message.text
        user_state[user_id] = 'waiting_phone'

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        phone_btn = types.KeyboardButton("Raqamimni ulashish", request_contact=True)
        markup.add(phone_btn)
        bot.send_message(message.chat.id, "Telefon raqamingizni kiriting:", reply_markup=markup)

    elif state == 'waiting_phone':
        if message.contact:
            user_data[user_id]['phone'] = message.contact.phone_number
        else:
            user_data[user_id]['phone'] = message.text

        user_state.pop(user_id)
        bot.send_message(message.chat.id, "Ma’lumotlar saqlandi ✅", reply_markup=get_main_menu())

# --- Kontaktni olish ---
@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    user_id = message.from_user.id
    if user_state.get(user_id) == 'waiting_phone':
        user_data[user_id]['phone'] = message.contact.phone_number
        user_state.pop(user_id)
        bot.send_message(message.chat.id, "Ma’lumotlar saqlandi ✅", reply_markup=get_main_menu())

# --- Hisobot tugmasi ---
@bot.message_handler(func=lambda m: m.text == "📊 Hisobot")
def show_report(message):
    user_id = message.from_user.id
    if user_id in user_data:
        data = user_data[user_id]
        bot.send_message(message.chat.id,
                         f"Ism: {data.get('first_name')}\n"
                         f"Familya: {data.get('last_name')}\n"
                         f"Telefon: {data.get('phone')}")
    else:
        bot.send_message(message.chat.id, "Siz hali ma’lumot kiritmagansiz.")

# --- Admin / Channel / Website tugmalari ---
@bot.message_handler(func=lambda m: m.text in ["👨‍💻 Admin", "📺 Our Channel", "🌐 Our Website"])
def handle_links(message):
    if message.text == "👨‍💻 Admin":
        bot.send_message(message.chat.id, "Admin: @Ronan_Smith")
    elif message.text == "📺 Our Channel":
        bot.send_message(message.chat.id, "📺 Channel: https://t.me/American_Life018")
    elif message.text == "🌐 Our Website":
        bot.send_message(message.chat.id, "🌐 Website: https://yourwebsite.com")

# --- Handlerlarni ro‘yxatdan o‘tkazish ---
register_reading_handlers(bot)
register_listening_handlers(bot)
register_writing_handlers(bot)
register_speaking_handler(bot)  # speaking tugmasini qo'shish

print("Bot ishga tushdi... ✅")
bot.polling()
