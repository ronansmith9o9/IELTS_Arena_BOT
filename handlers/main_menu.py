from telebot import types

def get_main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        types.KeyboardButton("📖 Reading"),
        types.KeyboardButton("🎧 Listening"),
        types.KeyboardButton("✍️ Writing"),
        types.KeyboardButton("🗣 Speaking"),
        types.KeyboardButton("📝 Full Mock"),
        types.KeyboardButton("👨‍💻 Admin"),
        types.KeyboardButton("📊 Reports"),
        types.KeyboardButton("📈 Statics"),
        types.KeyboardButton("📺 Our Channel"),
        types.KeyboardButton("🌐 Our Website"),
        types.KeyboardButton("💳 Wallet"),
    )
    return markup
