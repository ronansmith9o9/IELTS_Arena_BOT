import telebot
from telebot import types
from handlers.main_menu import get_main_menu
from handlers.reading import register_reading_handlers
from handlers.listening import register_listening_handlers
from handlers.writing import register_writing_handlers  # ✅ to‘g‘ri funksiya nomi

TOKEN = "8276217068:AAESR-xxhwcFaMf6zXIwQynlm3CN7LNiAFI"
bot = telebot.TeleBot(TOKEN)

# --- Handlerslarni ro‘yxatdan o‘tkazamiz ---
register_reading_handlers(bot)
register_listening_handlers(bot)
register_writing_handlers(bot)

# --- /start buyrug‘i ---
@bot.message_handler(commands=['start'])
def start(message):
    markup = get_main_menu()
    bot.send_message(
        chat_id=message.chat.id,
        text=f"Hello, {message.from_user.first_name}! Welcome to the IELTS preparation bot 🎯",
        reply_markup=markup
    )

# --- Qo‘shimcha tugmalar (Admin, Channel, Website) ---
@bot.message_handler(func=lambda message: message.text in ["👨‍💻 Admin", "📺 Our Channel", "🌐 Our Website"])
def handle_links(message):
    if message.text == "👨‍💻 Admin":
        bot.send_message(message.chat.id, "👨‍💻 Admin: @Ronan_Smith")
    elif message.text == "📺 Our Channel":
        bot.send_message(message.chat.id, "📺 Channel: https://t.me/American_Life018")
    elif message.text == "🌐 Our Website":
        bot.send_message(message.chat.id, "🌐 Website: https://yourwebsite.com")

print("✅ Bot ishga tushdi...")
bot.infinity_polling()
