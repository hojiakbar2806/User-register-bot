from telegram.ext import filters, ApplicationBuilder, CallbackQueryHandler, MessageHandler, CommandHandler

from config import steps, token
from function import main_menu
from handler.inline_handler import inline_handler
from handler.message_handler import message_handler

from database import BaseCRUD
users = BaseCRUD("users.db", "users")


async def start(update, context):
    context.user_data['edit_step'] = False
    chat_id = update.message.from_user.id
    users_list = users.get_all()

    user_exist = any(chat_id == i['chat_id'] for i in users_list)

    if user_exist:
        await main_menu(update, context)
    else:
        context.user_data['step'] = steps["first_name"]
        await update.message.reply_text(text="Enter your first name")

    print(user_exist)



if __name__ == "__main__":
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT, message_handler))
    app.add_handler(MessageHandler(filters.CONTACT, start))
    app.add_handler(MessageHandler(filters.LOCATION, start))
    app.add_handler(CallbackQueryHandler(inline_handler))

    app.run_polling()
