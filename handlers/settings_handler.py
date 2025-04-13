# handlers/settings_handler.py

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from config.config import SETTINGS, SETTINGS_IMAGE_DIR
from utils.font_formatter import to_small_caps
from utils.image_randomizer import get_random_image
from utils.message_cleaner import delete_message

async def show_settings(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()

    chat_id = query.message.chat_id
    user_id = query.from_user.id

    # Delete the previous welcome message
    if context.user_data.get("welcome_message_id"):
        await delete_message(context, chat_id, context.user_data["welcome_message_id"])
        context.user_data["welcome_message_id"] = None

    # Create settings message in small caps
    settings_message = to_small_caps(
        f"Configurations\n\n"
        f"Total Force Sub Channel: {SETTINGS['total_force_sub_channel']}\n"
        f"Total Admins: {SETTINGS['total_admins']}\n"
        f"Total Banned Users: {SETTINGS['total_banned_users']}\n"
        f"Auto Delete Mode: {SETTINGS['auto_delete_mode']}\n"
        f"Protect Content: {SETTINGS['protect_content']}\n"
        f"Hide Caption: {SETTINGS['hide_caption']}\n"
        f"Channel Button: {SETTINGS['channel_button']}\n"
        f"Request FSub Mode: {SETTINGS['request_fsub_mode']}"
    )

    # Create buttons for Back and Close
    keyboard = [
        [
            InlineKeyboardButton("Back", callback_data="back_to_welcome"),
            InlineKeyboardButton("Close", callback_data="close_message")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Get a random image from the settings directory
    image_path = get_random_image(SETTINGS_IMAGE_DIR)

    # Send the settings message with image and buttons
    if image_path:
        with open(image_path, 'rb') as photo:
            message = await context.bot.send_photo(
                chat_id=chat_id,
                photo=photo,
                caption=settings_message,
                reply_markup=reply_markup,
                parse_mode="HTML"
            )
    else:
        message = await context.bot.send_message(
            chat_id=chat_id,
            text=settings_message,
            reply_markup=reply_markup,
            parse_mode="HTML"
        )

    # Store the settings message ID
    context.user_data["settings_message_id"] = message.message_id
