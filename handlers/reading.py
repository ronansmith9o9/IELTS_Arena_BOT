from telebot import types
from handlers.main_menu import get_main_menu

passages = {
    "Passage 1": [f"Test {i}" for i in range(1, 51)],
    "Passage 2": [f"Test {i}" for i in range(1, 51)],
    "Passage 3": [f"Test {i}" for i in range(1, 51)],
}

full_reading_test = [f"Test {i}" for i in range(1, 31)]  # Oddiy Test 1-30

user_passage = {}

def register_reading_handlers(bot):

    @bot.message_handler(func=lambda message: message.text == "📖 Reading")
    def reading_menu(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(
            types.KeyboardButton("Passage 1"),
            types.KeyboardButton("Passage 2"),
            types.KeyboardButton("Passage 3"),
            types.KeyboardButton("Full Reading Test"),
            types.KeyboardButton("🔙 Back")
        )
        bot.send_message(message.chat.id, "Select a passage or full reading test:", reply_markup=markup)

    @bot.message_handler(func=lambda message: message.text in list(passages.keys()) + ["Full Reading Test", "🔙 Back"])
    def reading_selection(message):
        chat_id = message.chat.id
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)

        if message.text in passages:
            user_passage[chat_id] = message.text
            tests = passages[message.text]
            for i in range(0, len(tests), 5):
                markup.row(*[types.KeyboardButton(t) for t in tests[i:i+5]])
            markup.add(types.KeyboardButton("🔙 Back"))
            bot.send_message(chat_id, f"{message.text}: Select a test (1-50)", reply_markup=markup)

        elif message.text == "Full Reading Test":
            user_passage[chat_id] = "Full Reading Test"
            tests = full_reading_test
            for i in range(0, len(tests), 5):
                markup.row(*[types.KeyboardButton(t) for t in tests[i:i+5]])
            markup.add(types.KeyboardButton("🔙 Back"))
            bot.send_message(chat_id, "Full Reading Test: Select a test (1-30)", reply_markup=markup)

        elif message.text == "🔙 Back":
            if chat_id in user_passage:
                user_passage.pop(chat_id)
            markup = get_main_menu()
            bot.send_message(chat_id, "Back to main menu:", reply_markup=markup)

    @bot.message_handler(func=lambda message: message.text.startswith("Test"))
    def test_answer(message):
        bot.send_message(message.chat.id, f"Here is the answer/explanation for {message.text}")
