from telebot import types

def register_fullmock_handlers(bot, get_main_menu):
    """
    Full Mock Tests handler:
    - 4 Free tests (ReplyKeyboard)
    - 26 Paid tests (InlineKeyboard, 2 columns)
    - Charge button for each paid test
    - Auto-delete previous message when new one clicked
    """

    # --- Free tests (1–4) ---
    @bot.message_handler(func=lambda m: m.text == "📝 Full Mock")
    def full_mock_menu(message):
        free_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for i in range(1, 5):
            free_markup.add(f"Mock Test {i} ✅ Free")
        free_markup.add("➡ Paid Full Mock Tests")
        free_markup.add("⬅ Back")
        bot.send_message(message.chat.id, "Select a Free Mock Test:", reply_markup=free_markup)

    # --- Free test selection ---
    @bot.message_handler(func=lambda m: m.text.startswith("Mock Test") and "Free" in m.text)
    def free_mock_selection(message):
        bot.send_message(message.chat.id, f"You selected {message.text}. You can start this free test now!")

    # --- Paid tests list (2 columns x 13 rows) ---
    @bot.message_handler(func=lambda m: m.text == "➡ Paid Full Mock Tests")
    def paid_mock_menu(message):
        paid_markup = types.InlineKeyboardMarkup(row_width=2)
        buttons = []
        for i in range(5, 31):
            btn = types.InlineKeyboardButton(
                f"Mock Test {i} 💎 14,990 UZS",
                callback_data=f"paid_mock_{i}"
            )
            buttons.append(btn)
        paid_markup.add(*buttons)

        # Back button
        back_btn = types.InlineKeyboardButton("⬅ Back", callback_data="back_free")
        paid_markup.add(back_btn)

        bot.send_message(message.chat.id, "💵 Select a Paid Full Mock Test:", reply_markup=paid_markup)

    # --- Handle Paid test info ---
    @bot.callback_query_handler(func=lambda call: call.data.startswith("paid_mock_"))
    def handle_paid_mock(call):
        test_number = int(call.data.split("_")[2])
        bot.answer_callback_query(call.id)

        # Har bir mock test ma'lumoti
        test_info = (
            f"🧾 <b>Full Mock Test {test_number}</b>\n\n"
            f"📘 Includes:\n"
            f"• Listening Section 🎧\n"
            f"• Reading Section 📖\n"
            f"• Writing Section ✍️\n"
            f"• Speaking Section 🎤\n"
            f"• Writing and Speaking Feedback 🧠\n"
            f"• Overall band score 📊\n\n"
            f"💎 <b>Price:</b> 14,990 UZS"
        )

        # Inline tugma: Charge va Back
        info_markup = types.InlineKeyboardMarkup(row_width=1)
        charge_btn = types.InlineKeyboardButton("💳 Charge", callback_data=f"charge_{test_number}")
        back_btn = types.InlineKeyboardButton("⬅ Back to list", callback_data="back_to_paid")
        info_markup.add(charge_btn, back_btn)

        # Eski xabarni o‘chirib, yangisini chiqarish
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except:
            pass

        bot.send_message(call.message.chat.id, test_info, reply_markup=info_markup, parse_mode="HTML")

    # --- Charge button bosilganda ---
    @bot.callback_query_handler(func=lambda call: call.data.startswith("charge_"))
    def handle_charge(call):
        test_number = call.data.split("_")[1]
        bot.answer_callback_query(call.id)
        markup = types.InlineKeyboardMarkup()
        pay_btn = types.InlineKeyboardButton("💳 Pay via Click", url="https://click.uz/payment-link")
        markup.add(pay_btn)
        bot.send_message(
            call.message.chat.id,
            f"To pay for <b>Mock Test {test_number}</b>, click below 👇",
            parse_mode="HTML",
            reply_markup=markup
        )

    # --- Back to Paid list ---
    @bot.callback_query_handler(func=lambda call: call.data == "back_to_paid")
    def back_to_paid(call):
        bot.answer_callback_query(call.id)
        paid_markup = types.InlineKeyboardMarkup(row_width=2)
        buttons = []
        for i in range(5, 31):
            btn = types.InlineKeyboardButton(
                f"Mock Test {i} 💎 14,990 UZS",
                callback_data=f"paid_mock_{i}"
            )
            buttons.append(btn)
        paid_markup.add(*buttons)
        back_btn = types.InlineKeyboardButton("⬅ Back", callback_data="back_free")
        paid_markup.add(back_btn)

        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except:
            pass

        bot.send_message(call.message.chat.id, "💵 Select a Paid Full Mock Test:", reply_markup=paid_markup)

    # --- Back to Free menu ---
    @bot.callback_query_handler(func=lambda call: call.data == "back_free")
    def back_to_free(call):
        bot.answer_callback_query(call.id)
        free_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for i in range(1, 5):
            free_markup.add(f"Mock Test {i} ✅ Free")
        free_markup.add("➡ Paid Full Mock Tests")
        free_markup.add("⬅ Back")
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except:
            pass
        bot.send_message(call.message.chat.id, "Select a Free Mock Test:", reply_markup=free_markup)

    # --- Back to main menu ---
    @bot.message_handler(func=lambda m: m.text == "⬅ Back")
    def back_to_main(message):
        bot.send_message(message.chat.id, "Returning to Main Menu...", reply_markup=get_main_menu())
