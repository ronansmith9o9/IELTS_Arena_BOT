# from telebot import types

# def get_main_menu():
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     markup.add(
#         types.KeyboardButton("📖 Reading"),
#         types.KeyboardButton("🎧 Listening"),
#         types.KeyboardButton("✍️ Writing"),
#         types.KeyboardButton("🗣 Speaking"),
#         types.KeyboardButton("📝 Full Mock"),
#         types.KeyboardButton("📊 Reports"),
#         types.KeyboardButton("👨‍💻 Admin"),
#         types.KeyboardButton("📺 Our Channel"),
#         types.KeyboardButton("🌐 Our Website")
#     )
#     return markup

# def register_handlers(bot):
#     @bot.message_handler(commands=['start'])
#     def start(message):
#         markup = get_main_menu()
#         bot.send_message(
#             chat_id=message.chat.id,
#             text=f"Hello, {message.from_user.first_name}! Welcome to the IELTS preparation bot.",
#             reply_markup=markup
#         )
    
#     # Optional: start from Main Menu button
#     @bot.message_handler(func=lambda message: message.text == "🏠 Main Menu")
#     def start_from_button(message):
#         markup = get_main_menu()
#         bot.send_message(message.chat.id, "Main menu:", reply_markup=markup)



from telebot import types

def get_main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        types.KeyboardButton("📖 Reading"),
        types.KeyboardButton("🎧 Listening"),
        types.KeyboardButton("✍️ Writing"),
        types.KeyboardButton("🗣 Speaking"),
        types.KeyboardButton("📝 Full Mock"),
        types.KeyboardButton("📊 Reports"),
        types.KeyboardButton("👨‍💻 Admin"),
        types.KeyboardButton("📺 Our Channel"),
        types.KeyboardButton("🌐 Our Website")
    )
    return markup
