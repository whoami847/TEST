# handlers/welcome_handler.py

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from config.config import DEFAULT_WELCOME_MESSAGE, WELCOME_IMAGE_DIR
from utils.font_formatter import to_small_caps
from utils.image_randomizer import get_random_image
import os

async def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    
    # Store the user_id in context for later use (to track message IDs)
    if not context.user_data.get("welcome_message_id"):
        context.user_data["welcome_message_id"] = None

    # Get welcome message and format it in small caps
    welcome_message = to_small_caps(DEFAULT_WELCOME_MESSAGE)

    # Create buttons for About and Settings
    keyboard = [
        [
            InlineKeyboardButton("About Me", callback_data="show_about"),
            InlineKeyboardButton("Settings", callback_data="show_settings")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Get a random image from the welcome directory
    image_path = get_random_image(WELCOME_IMAGE_DIR)

    # Send the welcome message with image and buttons
    if image_path:
        with open(image_path, 'rb') as photo:
            message = await context.bot.send_photo(
                chat_id=chat_id,
                photo=photo,
                caption=welcome_message,
                reply_markup=reply_markup,
                parse_mode="HTML"
            )
    else:
        message = await context.bot.send_message(
            chat_id=chat_id,
            text=welcome_message,
            reply_markup=reply_markup,
            parse_mode="HTML"
        )

    # Store the message ID for deletion later
    context.user_data["welcome_message_id"] = message.message_id
