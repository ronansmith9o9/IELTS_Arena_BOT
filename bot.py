import telebot
from handlers.main_menu import register_handlers
from handlers.reading import register_reading_handlers
from handlers.listening import register_listening_handlers

TOKEN = "8276217068:AAESR-xxhwcFaMf6zXIwQynlm3CN7LNiAFI"
bot = telebot.TeleBot(TOKEN)


register_handlers(bot)
register_reading_handlers(bot)
register_listening_handlers(bot)

print("Bot ishga tushdi...")
bot.polling()
