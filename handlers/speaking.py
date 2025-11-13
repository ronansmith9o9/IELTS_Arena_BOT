from telebot import types

def register_speaking_handler(bot):
    @bot.message_handler(func=lambda m: m.text == "🗣 Speaking")  # KeyboardButton dan
    def show_speaking_info(message):
        # IELTS Speaking haqida xabarlar
        bot.send_message(message.chat.id,
                         "📌 IELTS Speaking Overview:\n\n"
                         "<b>Part 1:</b> Introduction & Interview\n"
                         "<b>Part 2:</b> Cue Card, 2-minute speech\n"
                         "<b>Part 3:</b> Discussion related to Part 2\n"
                         "<b>Full Speaking Mock:</b> Available\n"
                         "<b>Mocks:</b> Free and paid\n"
                         "<b>Paid Mocks:</b> Include feedback and overall speaking score\n"
                         "<b>Free mocks:</b> Give feedback and speaking score not included\n"
                         "Practice regularly to improve fluency and coherence.")

        # Inline tugma: Start Speaking
        markup = types.InlineKeyboardMarkup()
        start_btn = types.InlineKeyboardButton("Start Speaking", url="https://yourwebsite.com/speaking.html")
        markup.add(start_btn)

        bot.send_message(message.chat.id, "Click below to start practicing:", reply_markup=markup)
