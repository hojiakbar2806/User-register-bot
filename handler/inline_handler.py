from telegram import InlineKeyboardMarkup, ReplyKeyboardMarkup

from function import main_menu
from config import user_edit_btns, gender_btns, contact_btns
from database import BaseCRUD
users = BaseCRUD("users.db", "users")


async def inline_handler(update, context):
    query = update.callback_query
    chat_id = query.message.chat_id
    message_id = query.message.message_id

    if query.data == "edit_data":
        await query.message.edit_reply_markup(
            reply_markup=InlineKeyboardMarkup(user_edit_btns)
        )

    elif query.data == "edit_first_name":
        await query.message.edit_text("Enter First Name!")
        context.user_data['edit_step'] = True
        context.user_data['step'] = 1

    elif query.data == "edit_last_name":
        await query.message.edit_text("Enter Last Name!")
        context.user_data['edit_step'] = True
        context.user_data['step'] = 2

    elif query.data == "edit_age":
        await query.message.edit_text("Enter Age!")
        context.user_data['edit_step'] = True
        context.user_data['step'] = 3

    elif query.data == "edit_gender":
        await query.message.edit_text("Update your gender")
        await query.message.edit_text(text="Choose Your Gender!", reply_markup=ReplyKeyboardMarkup(
            gender_btns, resize_keyboard=True, one_time_keyboard=True))
        context.user_data['edit_step'] = True
        context.user_data['step'] = 4

    elif query.data == "edit_contact":
        await query.message.edit_text("Update your contact")
        await query.message.reply_text("Share Your Contact Or Send It!", reply_markup=ReplyKeyboardMarkup(
            contact_btns, resize_keyboard=True, one_time_keyboard=True))
        context.user_data['edit_step'] = True
        context.user_data['step'] = 5

    elif query.data == "main_menu":
        await main_menu(update, context, chat_id)
