# handlers/about_handler.py

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from config.config import ABOUT_IMAGE_DIR
from utils.font_formatter import to_small_caps
from utils.image_randomizer import get_random_image
from utils.message_cleaner import delete_message

async def show_about(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()

    chat_id = query.message.chat_id
    user_id = query.from_user.id

    # Delete the previous welcome message
    if context.user_data.get("welcome_message_id"):
        await delete_message(context, chat_id, context.user_data["welcome_message_id"])
        context.user_data["welcome_message_id"] = None

    # About message in small caps
    about_message = to_small_caps("My Name: FileShare Bot 3\n\nAdvance Features: Click Here\n\nOwner: King\n\nLanguage: Python 3\n\nLibrary: Pyrogram V2\n\nDatabase: Mongo DB\n\nDeveloper: @shidoteshika1")

    # Create buttons for Back and Close
    keyboard = [
        [
            InlineKeyboardButton("Back", callback_data="back_to_welcome"),
            InlineKeyboardButton("Close", callback_data="close_message")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Get a random image from the about directory
    image_path = get_random_image(ABOUT_IMAGE_DIR)

    # Send the about message with image and buttons
    if image_path:
        with open(image_path, 'rb') as photo:
            message = await context.bot.send_photo(
                chat_id=chat_id,
                photo=photo,
                caption=about_message,
                reply_markup=reply_markup,
                parse_mode="HTML"
            )
    else:
        message = await context.bot.send_message(
            chat_id=chat_id,
            text=about_message,
            reply_markup=reply_markup,
            parse_mode="HTML"
        )

    # Store the about message ID
    context.user_data["about_message_id"] = message.message_id
