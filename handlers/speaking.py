from telebot import types

def register_speaking_handler(bot):
    @bot.message_handler(func=lambda m: m.text == "🗣 Speaking")  # KeyboardButton dan
    def show_speaking_info(message):
        # IELTS Speaking haqida xabarlar
        speaking_text = (
            "📌 <b>IELTS Speaking Overview</b>\n\n"
            "💬 <b>Part 1:</b> Introduction & Interview\n"
            "💬 <b>Part 2:</b> Cue Card, 2-minute speech\n"
            "💬 <b>Part 3:</b> Discussion related to Part 2\n"
            "📝 <b>Full Speaking Mock:</b> Available\n"
            "🎯 <b>Mocks:</b> Free and Paid\n"
            "💎 <b>Paid Mocks:</b> Include feedback and overall speaking score\n"
            "🔓 <b>Free Mocks:</b> Feedback and speaking score not included"
        )

        # Inline tugma: Start Speaking
        markup = types.InlineKeyboardMarkup()
        start_btn = types.InlineKeyboardButton(
            "Start Speaking", url="https://yourwebsite.com/speaking.html"
        )
        markup.add(start_btn)

        # Xabar + inline tugma birga chiqadi
        bot.send_message(message.chat.id, speaking_text, reply_markup=markup, parse_mode='HTML')
