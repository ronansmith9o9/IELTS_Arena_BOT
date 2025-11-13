# from telebot import types
# from handlers.main_menu import get_main_menu

# def register_writing_handlers(bot):
#     # --- Writing bo‘limi asosiy menyusi ---
#     @bot.message_handler(func=lambda message: message.text == "📝 Writing")
#     def writing_menu(message):
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#         btn1 = types.KeyboardButton("📄 Task 1")
#         btn2 = types.KeyboardButton("🧾 Task 2")
#         btn3 = types.KeyboardButton("🧠 Full Writing Mock")
#         back = types.KeyboardButton("⬅️ Back")
#         markup.add(btn1, btn2, btn3, back)
#         bot.send_message(message.chat.id, "Choose a Writing Section 👇", reply_markup=markup)

#     # --- Task 1 bo‘limi ---
#     @bot.message_handler(func=lambda message: message.text == "📄 Task 1")
#     def writing_task1(message):
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)

#         buttons = [types.KeyboardButton(f"Task1 Test {i}") for i in range(1, 51)]
#         markup.add(*buttons)

#         back = types.KeyboardButton("⬅️ Back to Writing")
#         markup.add(back)

#         bot.send_message(message.chat.id, "📄 Choose Task 1 Test 👇", reply_markup=markup)

#     # --- Task 2 bo‘limi ---
#     @bot.message_handler(func=lambda message: message.text == "🧾 Task 2")
#     def writing_task2(message):
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)

#         buttons = [types.KeyboardButton(f"Task2 Test {i}") for i in range(1, 51)]
#         markup.add(*buttons)

#         back = types.KeyboardButton("⬅️ Back to Writing")
#         markup.add(back)

#         bot.send_message(message.chat.id, "🧾 Choose Task 2 Test 👇", reply_markup=markup)

#     # --- Full Writing Mock bo‘limi ---
#     @bot.message_handler(func=lambda message: message.text == "🧠 Full Writing Mock")
#     def writing_full_mock(message):
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)

#         buttons = [types.KeyboardButton(f"Full Writing {i}") for i in range(1, 31)]
#         markup.add(*buttons)

#         back = types.KeyboardButton("⬅️ Back to Writing")
#         markup.add(back)

#         bot.send_message(message.chat.id, "🧠 Choose Full Writing Test 👇", reply_markup=markup)

#     # --- Task1, Task2, FullWriting testlarini yuborish ---
#     @bot.message_handler(func=lambda message: message.text.startswith("Task1 Test"))
#     def send_task1_test(message):
#         test_number = message.text.split()[-1]
#         file_path = f"ielts_bot/writing/task1/test{test_number}.html"
#         try:
#             with open(file_path, "rb") as f:
#                 bot.send_document(message.chat.id, f)
#         except FileNotFoundError:
#             bot.send_message(message.chat.id, f"❌ Task1 Test {test_number} fayli topilmadi.")

#     @bot.message_handler(func=lambda message: message.text.startswith("Task2 Test"))
#     def send_task2_test(message):
#         test_number = message.text.split()[-1]
#         file_path = f"ielts_bot/writing/task2/test{test_number}.html"
#         try:
#             with open(file_path, "rb") as f:
#                 bot.send_document(message.chat.id, f)
#         except FileNotFoundError:
#             bot.send_message(message.chat.id, f"❌ Task2 Test {test_number} fayli topilmadi.")

#     @bot.message_handler(func=lambda message: message.text.startswith("Full Writing"))
#     def send_fullwriting_test(message):
#         test_number = message.text.split()[-1]
#         file_path = f"ielts_bot/writing/full/test{test_number}.html"
#         try:
#             with open(file_path, "rb") as f:
#                 bot.send_document(message.chat.id, f)
#         except FileNotFoundError:
#             bot.send_message(message.chat.id, f"❌ Full Writing {test_number} fayli topilmadi.")

#     # --- Back tugmalari ---
#     @bot.message_handler(func=lambda message: message.text == "⬅️ Back to Writing")
#     def back_to_writing(message):
#         writing_menu(message)


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

    # --- 📄 Task 1 (50 ta test) ---
    @bot.message_handler(func=lambda message: message.text == "📄 Task 1")
    def task1_menu(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)
        for i in range(1, 51):  # ✅ 50 test
            markup.insert(types.KeyboardButton(f"Task1 Test {i}"))
        markup.add(types.KeyboardButton("⬅️ Back to Writing"))
        bot.send_message(message.chat.id, "📄 Choose Task 1 Test 👇", reply_markup=markup)

    # --- 🧾 Task 2 (50 ta test) ---
    @bot.message_handler(func=lambda message: message.text == "🧾 Task 2")
    def task2_menu(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)
        for i in range(1, 51):  # ✅ 50 test
            markup.insert(types.KeyboardButton(f"Task2 Test {i}"))
        markup.add(types.KeyboardButton("⬅️ Back to Writing"))
        bot.send_message(message.chat.id, "🧾 Choose Task 2 Test 👇", reply_markup=markup)

    # --- 🧠 Full Writing Mock (30 ta test) ---
    @bot.message_handler(func=lambda message: message.text == "🧠 Full Writing Mock")
    def fullwriting_menu(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)
        for i in range(1, 31):  # ✅ 30 test
            markup.insert(types.KeyboardButton(f"Full Writing {i}"))
        markup.add(types.KeyboardButton("⬅️ Back to Writing"))
        bot.send_message(message.chat.id, "🧠 Choose Full Writing Test 👇", reply_markup=markup)

    # --- 📂 Fayllarni yuborish qismi ---
    @bot.message_handler(func=lambda message: message.text.startswith("Task1 Test"))
    def send_task1(message):
        num = message.text.split()[-1]
        path = f"ielts_bot/writing/task1/test{num}.html"
        if os.path.exists(path):
            with open(path, "rb") as f:
                bot.send_document(message.chat.id, f)
        else:
            bot.send_message(message.chat.id, f"❌ Task1 Test {num} fayli topilmadi.")

    @bot.message_handler(func=lambda message: message.text.startswith("Task2 Test"))
    def send_task2(message):
        num = message.text.split()[-1]
        path = f"ielts_bot/writing/task2/test{num}.html"
        if os.path.exists(path):
            with open(path, "rb") as f:
                bot.send_document(message.chat.id, f)
        else:
            bot.send_message(message.chat.id, f"❌ Task2 Test {num} fayli topilmadi.")

    @bot.message_handler(func=lambda message: message.text.startswith("Full Writing"))
    def send_fullwriting(message):
        num = message.text.split()[-1]
        path = f"ielts_bot/writing/full/test{num}.html"
        if os.path.exists(path):
            with open(path, "rb") as f:
                bot.send_document(message.chat.id, f)
        else:
            bot.send_message(message.chat.id, f"❌ Full Writing {num} fayli topilmadi.")

    # --- 🔙 Back tugmalari ---
    @bot.message_handler(func=lambda message: message.text == "⬅️ Back to Writing")
    def back_to_writing(message):
        writing_menu(message)

    @bot.message_handler(func=lambda message: message.text == "⬅️ Back")
    def back_to_main(message):
        markup = get_main_menu()
        bot.send_message(message.chat.id, "🏠 Back to main menu:", reply_markup=markup)
