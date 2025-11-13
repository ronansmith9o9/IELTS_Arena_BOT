import telebot
from telebot import types
from handlers.main_menu import get_main_menu
from handlers.reading import register_reading_handlers
from handlers.listening import register_listening_handlers
from handlers.writing import register_writing_handlers
from handlers.speaking import register_speaking_handler
from handlers.fullmock import register_fullmock_handlers
from datetime import datetime, timedelta

TOKEN = "8256624974:AAG9sPHDkkxO9OksxFS0bs52dHwOaCCRGW0"
CHANNEL = "@American_Life018"

bot = telebot.TeleBot(TOKEN)

# --- User data storage ---
user_data = {}   # {user_id: {'first_name':..., 'last_name':..., 'phone':..., 'wallet':0, 'joined':datetime}}
user_state = {}  # {user_id: 'waiting_name' / 'waiting_family' / 'waiting_phone'}

# --- Check subscription ---
def is_subscribed(user_id):
    try:
        status = bot.get_chat_member(CHANNEL, user_id).status
        return status in ['member', 'creator', 'administrator']
    except:
        return False

# --- /start command ---
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id

    if not is_subscribed(user_id):
        markup = types.InlineKeyboardMarkup()
        subscribe_btn = types.InlineKeyboardButton("Subscribe", url=f"https://t.me/{CHANNEL[1:]}")
        confirm_btn = types.InlineKeyboardButton("Confirm ✅", callback_data="confirm_sub")
        markup.add(subscribe_btn, confirm_btn)
        bot.send_message(message.chat.id,
                         "Please subscribe to the channel and confirm 👇",
                         reply_markup=markup)
        return

    if user_id not in user_data:
        user_data[user_id] = {'wallet':0, 'joined':datetime.now()}
        bot.send_message(message.chat.id, "Welcome! Please enter your first name:")
        user_state[user_id] = 'waiting_name'
        return

    bot.send_message(message.chat.id, "Welcome back to IELTS Arena Bot!", reply_markup=get_main_menu())

# --- Confirm subscription callback ---
@bot.callback_query_handler(func=lambda call: call.data == "confirm_sub")
def confirm_subscription(call):
    user_id = call.from_user.id
    if is_subscribed(user_id):
        bot.answer_callback_query(call.id, "Subscription confirmed ✅")
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except:
            pass

        if user_id not in user_data:
            user_data[user_id] = {'wallet':0, 'joined':datetime.now()}
            bot.send_message(call.message.chat.id, "Welcome! Please enter your first name:")
            user_state[user_id] = 'waiting_name'
        else:
            bot.send_message(call.message.chat.id, "Welcome back to IELTS Arena Bot!", reply_markup=get_main_menu())
    else:
        bot.answer_callback_query(call.id, "You are not subscribed ❌")

# --- Handle user info ---
@bot.message_handler(func=lambda m: user_state.get(m.from_user.id) is not None)
def handle_user_info(message):
    user_id = message.from_user.id
    state = user_state.get(user_id)

    if state == 'waiting_name':
        user_data[user_id]['first_name'] = message.text
        user_state[user_id] = 'waiting_family'
        bot.send_message(message.chat.id, "Please enter your last name:")

    elif state == 'waiting_family':
        user_data[user_id]['last_name'] = message.text
        user_state[user_id] = 'waiting_phone'

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        phone_btn = types.KeyboardButton("Share my phone number", request_contact=True)
        markup.add(phone_btn)
        bot.send_message(message.chat.id, "Please share your phone number:", reply_markup=markup)

    elif state == 'waiting_phone':
        if message.contact:
            user_data[user_id]['phone'] = message.contact.phone_number
        else:
            user_data[user_id]['phone'] = message.text

        user_state.pop(user_id)
        bot.send_message(message.chat.id, "Data saved ✅", reply_markup=get_main_menu())

# --- Handle contact ---
@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    user_id = message.from_user.id
    if user_state.get(user_id) == 'waiting_phone':
        user_data[user_id]['phone'] = message.contact.phone_number
        user_state.pop(user_id)
        bot.send_message(message.chat.id, "Data saved ✅", reply_markup=get_main_menu())

# --- Reports menu ---
@bot.message_handler(func=lambda m: m.text == "📊 Reports")
def show_report(message):
    user_id = message.from_user.id
    if user_id in user_data:
        data = user_data[user_id]
        report_text = (
            f"First Name: {data.get('first_name')}\n"
            f"Last Name: {data.get('last_name')}\n"
            f"Phone: {data.get('phone')}"
        )
    else:
        report_text = "You haven't entered your data yet."

    markup = types.InlineKeyboardMarkup()
    change_btn = types.InlineKeyboardButton("Change", callback_data="change_info")
    markup.add(change_btn)
    bot.send_message(message.chat.id, report_text, reply_markup=markup)

# --- Change info ---
@bot.callback_query_handler(func=lambda call: call.data == "change_info")
def change_info(call):
    user_id = call.from_user.id
    try:
        bot.delete_message(call.message.chat.id, call.message.message_id)
    except:
        pass
    bot.send_message(call.message.chat.id, "Please enter your new first name:")
    user_state[user_id] = 'waiting_name'

# --- Wallet menu ---
@bot.message_handler(func=lambda m: m.text == "💰 Wallet")
def wallet_menu(message):
    user_id = message.from_user.id
    wallet_balance = user_data.get(user_id, {}).get('wallet', 0)

    text = f"Your current wallet balance: {wallet_balance} UZS"
    markup = types.InlineKeyboardMarkup()
    pay_btn = types.InlineKeyboardButton("💳 Pay / Top Up Wallet", url="https://click.uz/payment-link")
    markup.add(pay_btn)

    bot.send_message(message.chat.id, text, reply_markup=markup)

# --- Statistics menu ---
@bot.message_handler(func=lambda m: m.text == "📈 Statistics")
def show_statistics(message):
    total_users = len(user_data)
    now = datetime.now()
    yearly_users = sum(1 for u in user_data.values() if u['joined'].year == now.year)
    monthly_users = sum(1 for u in user_data.values() if u['joined'].month == now.month and u['joined'].year == now.year)
    weekly_users = sum(1 for u in user_data.values() if u['joined'] >= now - timedelta(days=7))
    daily_users = sum(1 for u in user_data.values() if u['joined'].date() == now.date())

    text = (
        f"📊 Total Users: {total_users}\n"
        f"🗓 Yearly Users: {yearly_users}\n"
        f"📅 Monthly Users: {monthly_users}\n"
        f"🗓 Weekly Users: {weekly_users}\n"
        f"📆 Daily Users: {daily_users}\n\n"
    )

    for uid, u in user_data.items():
        duration = datetime.now() - u['joined']
        days = duration.days
        hours = duration.seconds // 3600
        minutes = (duration.seconds % 3600) // 60
        text += f"User {u.get('first_name')} joined {days}d {hours}h {minutes}m ago\n"

    bot.send_message(message.chat.id, text)

# --- Admin / Channel / Website ---
@bot.message_handler(func=lambda m: m.text in ["👨‍💻 Admin", "📺 Our Channel", "🌐 Our Website"])
def handle_links(message):
    if message.text == "👨‍💻 Admin":
        bot.send_message(message.chat.id, "Admin: @Ronan_Smith")
    elif message.text == "📺 Our Channel":
        bot.send_message(message.chat.id, "📺 Channel: https://t.me/American_Life018")
    elif message.text == "🌐 Our Website":
        bot.send_message(message.chat.id, "🌐 Website: https://yourwebsite.com")

# --- Register other handlers ---
register_reading_handlers(bot)
register_listening_handlers(bot)
register_writing_handlers(bot)
register_speaking_handler(bot)
register_fullmock_handlers(bot, get_main_menu)

print("Bot is running... ✅")
bot.polling()
