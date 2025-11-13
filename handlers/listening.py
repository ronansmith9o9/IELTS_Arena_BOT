# from telebot import types
# from handlers.main_menu import get_main_menu

# sections = {
#     "Section 1": [f"Test {i}" for i in range(1, 51)],
#     "Section 2": [f"Test {i}" for i in range(1, 51)],
#     "Section 3": [f"Test {i}" for i in range(1, 51)],
#     "Section 4": [f"Test {i}" for i in range(1, 51)],
# }

# full_listening_test = [f"Test {i}" for i in range(1, 31)] 

# user_section = {}

# def register_listening_handlers(bot):

#     @bot.message_handler(func=lambda message: message.text == "🎧 Listening")
#     def listening_menu(message):
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#         markup.add(
#             types.KeyboardButton("Section 1"),
#             types.KeyboardButton("Section 2"),
#             types.KeyboardButton("Section 3"),
#             types.KeyboardButton("Section 4"),
#             types.KeyboardButton("Full Listening Test"),
#             types.KeyboardButton("🔙 Back")
#         )
#         bot.send_message(message.chat.id, "Select a section or full listening test:", reply_markup=markup)

#     @bot.message_handler(func=lambda message: message.text in list(sections.keys()) + ["Full Listening Test", "🔙 Back"])
#     def listening_selection(message):
#         chat_id = message.chat.id
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)

#         if message.text in sections:
#             user_section[chat_id] = message.text
#             tests = sections[message.text]
#             for i in range(0, len(tests), 5):
#                 markup.row(*[types.KeyboardButton(t) for t in tests[i:i+5]])
#             markup.add(types.KeyboardButton("🔙 Back"))
#             bot.send_message(chat_id, f"{message.text}: Select a test (1-50)", reply_markup=markup)

#         elif message.text == "Full Listening Test":
#             user_section[chat_id] = "Full Listening Test"
#             tests = full_listening_test
#             for i in range(0, len(tests), 5):
#                 markup.row(*[types.KeyboardButton(t) for t in tests[i:i+5]])
#             markup.add(types.KeyboardButton("🔙 Back"))
#             bot.send_message(chat_id, "Full Listening Test: Select a test (1-30)", reply_markup=markup)

#         elif message.text == "🔙 Back":
#             if chat_id in user_section:
#                 user_section.pop(chat_id)
#             markup = get_main_menu()
#             bot.send_message(chat_id, "Back to main menu:", reply_markup=markup)

#     @bot.message_handler(func=lambda message: message.text.startswith("Test"))
#     def test_answer(message):
#         bot.send_message(message.chat.id, f"Here is the answer/explanation for {message.text}")



from telebot import types
from handlers.main_menu import get_main_menu

sections = {
    "Section 1": [f"Test {i}" for i in range(1, 51)],
    "Section 2": [f"Test {i}" for i in range(1, 51)],
    "Section 3": [f"Test {i}" for i in range(1, 51)],
    "Section 4": [f"Test {i}" for i in range(1, 51)],
}

full_listening_test = [f"Test {i}" for i in range(1, 31)]
user_section = {}

def register_listening_handlers(bot):

    @bot.message_handler(func=lambda message: message.text == "🎧 Listening")
    def listening_menu(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(
            types.KeyboardButton("Section 1"),
            types.KeyboardButton("Section 2"),
            types.KeyboardButton("Section 3"),
            types.KeyboardButton("Section 4"),
            types.KeyboardButton("Full Listening Test"),
            types.KeyboardButton("🔙 Back")
        )
        bot.send_message(message.chat.id, "Select a section or full listening test:", reply_markup=markup)

    @bot.message_handler(func=lambda message: message.text in list(sections.keys()) + ["Full Listening Test", "🔙 Back"])
    def listening_selection(message):
        chat_id = message.chat.id
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)

        if message.text in sections:
            user_section[chat_id] = message.text
            for i in range(0, 50, 5):
                markup.row(*[types.KeyboardButton(f"Test {j}") for j in range(i + 1, i + 6)])
            markup.add(types.KeyboardButton("🔙 Back"))
            bot.send_message(chat_id, f"{message.text}: Select a test (1–50)", reply_markup=markup)

        elif message.text == "Full Listening Test":
            user_section[chat_id] = "Full Listening Test"
            for i in range(0, 30, 5):
                markup.row(*[types.KeyboardButton(f"Test {j}") for j in range(i + 1, i + 6)])
            markup.add(types.KeyboardButton("🔙 Back"))
            bot.send_message(chat_id, "Full Listening Test: Select a test (1–30)", reply_markup=markup)

        elif message.text == "🔙 Back":
            user_section.pop(chat_id, None)
            markup = get_main_menu()
            bot.send_message(chat_id, "Back to main menu:", reply_markup=markup)

    @bot.message_handler(func=lambda message: message.text.startswith("Test "))
    def test_answer(message):
        bot.send_message(message.chat.id, f"🎧 Here is Listening {message.text}")
