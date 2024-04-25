from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup
from database import BaseCRUD
from config import steps, gender_btns, info_edit_btns
from function import send_my_info

users = BaseCRUD("users.db", "users")


async def get_first_name(update, context):
    message = update.message.text
    chat_id = update.message.from_user.id
    context.user_data['first_name'] = message
    if context.user_data['edit_step']:
        users.update(chat_id, first_name=message)
        context.user_data['edit_step'] = False
        await update.message.reply_text(
            text="First name has been updated",
            reply_markup=ReplyKeyboardRemove()
        )
        await send_my_info(update, context)
    else:
        context.user_data['step'] = steps["last_name"]
        await update.message.reply_text(
            text="Enter your last Name:",
            reply_markup=ReplyKeyboardRemove()
        )


async def get_last_name(update, context):
    message = update.message.text
    chat_id = update.message.from_user.id
    context.user_data['last_name'] = message
    if context.user_data['edit_step']:
        users.update(chat_id, last_name=message)
        context.user_data['edit_step'] = False
        await update.message.reply_text(
            text="Last name has been updated",
            reply_markup=ReplyKeyboardRemove()
        )
        await send_my_info(update, context)
    else:
        context.user_data['step'] = steps["age"]
        await update.message.reply_text(
            text="Enter your age:",
            reply_markup=ReplyKeyboardRemove()
        )


async def get_age(update, context):
    message = update.message.text
    try:
        age = int(message)
        if age <= 0 or age > 150:
            raise ValueError
    except ValueError:
        await update.message.reply_text(
            text="Please enter a valid age (1-150)."
        )
        return

    chat_id = update.message.from_user.id
    context.user_data['age'] = age
    if context.user_data.get('edit_step', False):
        users.update(chat_id, age=age)
        context.user_data['edit_step'] = False
        await update.message.reply_text(
            text="Age has been updated",
            reply_markup=ReplyKeyboardRemove()
        )
        await send_my_info(update, context)
    else:
        context.user_data['step'] = steps["gender"]
        await update.message.reply_text(
            text='Enter your gender "Male/Female"',
            reply_markup=ReplyKeyboardMarkup(
                gender_btns,
                one_time_keyboard=True,
                resize_keyboard=True
            )
        )


async def get_gender(update, context):
    message = update.message.text
    chat_id = update.message.from_user.id
    context.user_data['gender'] = message
    if context.user_data['edit_step']:
        users.update(chat_id, gender=message)
        context.user_data['edit_step'] = False
        await update.message.reply_text(
            text="Gender has been updated",
            reply_markup=ReplyKeyboardRemove()
        )
        await send_my_info(update, context)
    else:
        context.user_data['step'] = steps["phone_number"]
        await update.message.reply_text(
            text="Enter your phone number ex:+998#########",
            reply_markup=ReplyKeyboardRemove()
        )


async def get_phone_number(update, context):
    message = update.message.text
    chat_id = update.message.from_user.id
    context.user_data['phone_number'] = message
    if context.user_data['edit_step']:
        users.update(chat_id, phone_number=message)
        context.user_data['edit_step'] = False
        await update.message.reply_text(
            text="Contact has been updated",
            reply_markup=ReplyKeyboardRemove()
        )
        await send_my_info(update, context)
    else:
        context.user_data['step'] = steps["location"]
        await update.message.reply_text(
            text='Enter your address "city/region"',
            reply_markup=ReplyKeyboardRemove()
        )


async def get_address(update, context):
    message = update.message.text
    chat_id = update.message.from_user.id
    context.user_data['location'] = message
    if context.user_data['edit_step']:
        users.update(chat_id, phone_number=message)
        context.user_data['edit_step'] = False
        await update.message.reply_text(
            text="Address has been updated",
            reply_markup=ReplyKeyboardRemove()
        )
        await send_my_info(update, context)
    else:
        context.user_data['step'] = 0
        reply_markup = ReplyKeyboardMarkup(
            info_edit_btns,
            one_time_keyboard=True,
            resize_keyboard=True
        )
        await update.message.reply_text(
            text="Do you want to save the information?", reply_markup=reply_markup)
