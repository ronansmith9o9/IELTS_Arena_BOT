# from telebot import types

# def register_handlers(bot):
#     """Main menu handlerlarini ro'yxatdan o'tkazish"""

#     # /start command
#     @bot.message_handler(commands=['start'])
#     def start(message):
#         # Reply keyboard yaratish
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

#         # Keyboard tugmalari
#         reading = types.KeyboardButton("📖 Reading")
#         listening = types.KeyboardButton("🎧 Listening")
#         writing = types.KeyboardButton("✍️ Writing")
#         speaking = types.KeyboardButton("🗣 Speaking")
#         full_mock = types.KeyboardButton("📝 Full Mock")
#         reports = types.KeyboardButton("📊 Reports")
#         channel = types.KeyboardButton("📺 Our Channel")
#         website = types.KeyboardButton("🌐 Our Website")

#         markup.add(reading, listening, writing, speaking, full_mock, reports, channel, website)

#         bot.send_message(
#             chat_id=message.chat.id,
#             text=f"Hello, {message.from_user.first_name}! Welcome to the IELTS preparation bot.",
#             reply_markup=markup  # Shu joyda keyboard xabar pastida chiqadi
#         )

#     # Foydalanuvchi tugmalarni bosganda
    # @bot.message_handler(func=lambda message: True)
    # def handle_buttons(message):
    #     text = message.text

    #     if text == "📖 Reading":
    #         bot.send_message(message.chat.id, "📖 Reading section: practice tests and exercises.")
    #     elif text == "🎧 Listening":
    #         bot.send_message(message.chat.id, "🎧 Listening section: audio exercises.")
    #     elif text == "✍️ Writing":
    #         bot.send_message(message.chat.id, "✍️ Writing section: essays and tasks.")
    #     elif text == "🗣 Speaking":
    #         bot.send_message(message.chat.id, "🗣 Speaking section: questions and sample answers.")
    #     elif text == "📝 Full Mock":
    #         bot.send_message(message.chat.id, "📝 Full Mock: complete IELTS test.")
    #     elif text == "📊 Reports":
    #         bot.send_message(message.chat.id, "📊 Reports: results and analysis.")
    #     elif text == "📺 Our Channel":
    #         bot.send_message(message.chat.id, "Check our channel: https://t.me/YourChannel")
    #     elif text == "🌐 Our Website":
    #         bot.send_message(message.chat.id, "Visit our website: https://yourwebsite.com")
    #     else:
    #         bot.send_message(message.chat.id, "Please choose an option from the menu below.")

from telebot import types

def get_main_menu():
    """Return main menu keyboard"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    reading = types.KeyboardButton("📖 Reading")
    listening = types.KeyboardButton("🎧 Listening")
    writing = types.KeyboardButton("✍️ Writing")
    speaking = types.KeyboardButton("🗣 Speaking")
    full_mock = types.KeyboardButton("📝 Full Mock")
    reports = types.KeyboardButton("📊 Reports")
    admin = types.KeyboardButton("📊 Admin")
    channel = types.KeyboardButton("📺 Our Channel")
    website = types.KeyboardButton("🌐 Our Website")

    markup.add(reading, listening, writing, speaking, full_mock, reports, admin, channel, website)
    return markup

def register_handlers(bot):
    """Main menu start handler"""
    @bot.message_handler(commands=['start'])
    def start(message):
        markup = get_main_menu()
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Hello, {message.from_user.first_name}! Welcome to the IELTS preparation bot.",
            reply_markup=markup
        )
