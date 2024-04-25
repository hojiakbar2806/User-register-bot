from config import steps
from function import main_menu, send_my_info, send_to_db
from register import get_address, get_age, get_first_name, get_gender, get_last_name, get_phone_number


async def message_handler(update, context):
    message = update.message.text
    step = context.user_data.get("step", 0)
    if step == steps["first_name"]:
        await get_first_name(update, context)
    elif step == steps["last_name"]:
        await get_last_name(update, context)
    elif step == steps["age"]:
        await get_age(update, context)
    elif step == steps["gender"]:
        await get_gender(update, context)
    elif step == steps["phone_number"]:
        await get_phone_number(update, context)
    elif step == steps["location"]:
        await get_address(update, context)
    elif message == "Save":
        await send_to_db(update, context)
    elif step == steps["send_to_base"]:
        await main_menu(update, context)
    elif message == "My info":
        await send_my_info(update, context)
