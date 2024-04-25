from telegram import InlineKeyboardMarkup, ReplyKeyboardRemove, ReplyKeyboardMarkup

from config import steps, info_btns, gender_btns, info_edit_btns, main_btns
from database import BaseCRUD
users = BaseCRUD("users.db", "users")


async def send_to_db(update, context):
    chat_id = update.message.from_user.id
    user_name = update.message.from_user.username
    data = context.user_data
    try:
        users.insert(
            first_name=data["first_name"],
            last_name=data["last_name"],
            age=data["age"],
            gender=data["gender"],
            phone_number=data["phone_number"],
            location=data["location"],
            latitude=data.get("latitude", None),
            longitude=data.get("longitude", None),
            chat_id=chat_id,
            user_name=user_name,
        )
        await update.message.reply_text(
            text="Saved to base",
            reply_markup=ReplyKeyboardRemove()
        )
        await main_menu(update, context)
    except Exception as e:
        await update.message.reply_text(
            text="Some thing went error or no data",
            reply_markup=ReplyKeyboardRemove()
        )
        print(e)
        await main_menu(update, context)
    context.user_data['step'] = steps["main"]


async def main_menu(update, context):
    reply_markup = ReplyKeyboardMarkup(
        main_btns,
        one_time_keyboard=True,
        resize_keyboard=True
    )
    await update.message.reply_text(text="Main menu", reply_markup=reply_markup)


async def send_my_info(update, context):
    chat_id = update.message.from_user.id
    try:
        user = users.get(chat_id)
        msg = await update.message.reply_text(
            text="🕓",
            reply_markup=ReplyKeyboardRemove(),
        )
        await context.bot.delete_message(chat_id=update.message.chat_id, message_id=msg.message_id)
        await context.bot.send_message(
            chat_id,
            text=(
                f"<b>First Name</b>: {user['first_name']}\n"
                f"<b>Last Name</b>: {user['last_name']}\n"
                f"<b>Phone Number</b>: {user['phone_number']}\n"
                f"<b>Gender</b>: {user['gender']}\n"
                f"<b>Location</b>: {user['location']}\n"
                f"<b>Age</b>: {user['age']}\n"
            ),
            reply_markup=InlineKeyboardMarkup(info_btns),
            parse_mode="HTML"
        )
    except Exception as e:
        await context.bot.send_message(
            chat_id,
            f"Something went error or no data"
        )


async def remove_inline(context, chat_id, message_id):
    await context.bot.delete_message(chat_id, message_id)
