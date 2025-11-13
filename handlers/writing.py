from telebot import types
import os
from handlers.main_menu import get_main_menu

def register_writing_handlers(bot):
    # --- Writing asosiy menyusi ---
    @bot.message_handler(func=lambda message: message.text == "✍️ Writing")
    def writing_menu(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(
            types.KeyboardButton("📄 Task 1"),
            types.KeyboardButton("🧾 Task 2"),
            types.KeyboardButton("🧠 Full Writing Mock"),
            types.KeyboardButton("⬅️ Back")
        )
        bot.send_message(message.chat.id, "✍️ Choose a Writing section 👇", reply_markup=markup)

    # --- Task 1 (50 ta test) ---
    @bot.message_handler(func=lambda message: message.text == "📄 Task 1")
    def task1_menu(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)
        # 50 ta button qo‘shish
        buttons = [types.KeyboardButton(f"Test {i}") for i in range(1, 51)]
        markup.add(*buttons)
        markup.add(types.KeyboardButton("⬅️ Back to Writing"))
        bot.send_message(message.chat.id, "📄 Choose Task 1 Test 👇", reply_markup=markup)

    # --- Task 2 (50 ta test) ---
    @bot.message_handler(func=lambda message: message.text == "🧾 Task 2")
    def task2_menu(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)
        buttons = [types.KeyboardButton(f"Test {i}") for i in range(1, 51)]
        markup.add(*buttons)
        markup.add(types.KeyboardButton("⬅️ Back to Writing"))
        bot.send_message(message.chat.id, "🧾 Choose Task 2 Test 👇", reply_markup=markup)

    # --- Full Writing Mock (30 ta test) ---
    @bot.message_handler(func=lambda message: message.text == "🧠 Full Writing Mock")
    def fullwriting_menu(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)
        buttons = [types.KeyboardButton(f"Test {i}") for i in range(1, 31)]
        markup.add(*buttons)
        markup.add(types.KeyboardButton("⬅️ Back to Writing"))
        bot.send_message(message.chat.id, "🧠 Choose Full Writing Test 👇", reply_markup=markup)

    # --- Fayllarni yuborish handlerlari ---
    @bot.message_handler(func=lambda message: message.text.startswith("Test"))
    def send_task1(message):
        num = message.text.split()[-1]
        path = f"ielts_bot/writing/task1/test{num}.html"
        if os.path.exists(path):
            with open(path, "rb") as f:
                bot.send_document(message.chat.id, f)
        else:
            bot.send_message(message.chat.id, f"❌ Task1 Test {num} fayli topilmadi.")

    @bot.message_handler(func=lambda message: message.text.startswith("Test"))
    def send_task2(message):
        num = message.text.split()[-1]
        path = f"ielts_bot/writing/task2/test{num}.html"
        if os.path.exists(path):
            with open(path, "rb") as f:
                bot.send_document(message.chat.id, f)
        else:
            bot.send_message(message.chat.id, f"❌ Task2 Test {num} fayli topilmadi.")

    @bot.message_handler(func=lambda message: message.text.startswith("Test"))
    def send_fullwriting(message):
        num = message.text.split()[-1]
        path = f"ielts_bot/writing/full/test{num}.html"
        if os.path.exists(path):
            with open(path, "rb") as f:
                bot.send_document(message.chat.id, f)
        else:
            bot.send_message(message.chat.id, f"❌ Full Writing Mock {num} fayli topilmadi.")

    # --- Back tugmalari ---
    @bot.message_handler(func=lambda message: message.text == "⬅️ Back to Writing")
    def back_to_writing(message):
        writing_menu(message)

    @bot.message_handler(func=lambda message: message.text == "⬅️ Back")
    def back_to_main(message):
        markup = get_main_menu()
        bot.send_message(message.chat.id, "🏠 Back to main menu:", reply_markup=markup)
