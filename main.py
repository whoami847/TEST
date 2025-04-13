# main.py

from telegram import Update  # Update ইমপোর্ট করা হলো
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, filters, CallbackContext  # CallbackContext ইমপোর্ট করা আছে
from config.config import BOT_TOKEN
from handlers.welcome_handler import start
from handlers.about_handler import show_about
from handlers.settings_handler import show_settings
from handlers.admin_handler import force_sub, add_force_sub, remove_force_sub
from handlers.force_sub_handler import check_force_sub
from utils.message_cleaner import delete_message

async def back_to_welcome(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()

    chat_id = query.message.chat_id

    # Delete the current about/settings message
    if context.user_data.get("about_message_id"):
        await delete_message(context, chat_id, context.user_data["about_message_id"])
        context.user_data["about_message_id"] = None
    if context.user_data.get("settings_message_id"):
        await delete_message(context, chat_id, context.user_data["settings_message_id"])
        context.user_data["settings_message_id"] = None

    # Show the welcome message again
    await start(update, context)

async def close_message(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()

    chat_id = query.message.chat_id

    # Delete the current about/settings message
    if context.user_data.get("about_message_id"):
        await delete_message(context, chat_id, context.user_data["about_message_id"])
        context.user_data["about_message_id"] = None
    if context.user_data.get("settings_message_id"):
        await delete_message(context, chat_id, context.user_data["settings_message_id"])
        context.user_data["settings_message_id"] = None

async def pre_check(update: Update, context: CallbackContext):
    return await check_force_sub(update, context)

def main():
    # Create the Application
    app = Application.builder().token(BOT_TOKEN).build()

    # Add handlers
    app.add_handler(CommandHandler("start", start, filters=filters.UpdateType.MESSAGE & ~filters.UpdateType.EDITED, block=False))
    app.add_handler(CommandHandler("force_sub", force_sub, filters=filters.UpdateType.MESSAGE & ~filters.UpdateType.EDITED, block=False))
    app.add_handler(CommandHandler("req_force_sub_add", add_force_sub, filters=filters.UpdateType.MESSAGE & ~filters.UpdateType.EDITED, block=False))
    app.add_handler(CommandHandler("req_force_sub_remv", remove_force_sub, filters=filters.UpdateType.MESSAGE & ~filters.UpdateType.EDITED, block=False))
    app.add_handler(CallbackQueryHandler(show_about, pattern="show_about"))
    app.add_handler(CallbackQueryHandler(show_settings, pattern="show_settings"))
    app.add_handler(CallbackQueryHandler(back_to_welcome, pattern="back_to_welcome"))
    app.add_handler(CallbackQueryHandler(close_message, pattern="close_message"))

    # Add pre-check for force subscription
    app.add_handler(CommandHandler("start", start, filters=filters.UpdateType.MESSAGE & ~filters.UpdateType.EDITED, block=False), group=0)
    app.pre_check = pre_check

    # Start the bot
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
