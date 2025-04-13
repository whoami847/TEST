# handlers/force_sub_handler.py

import json
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from config.config import FORCE_SUB_ENABLED, FORCE_SUB_FILE
from utils.font_formatter import to_small_caps

async def check_force_sub(update: Update, context: CallbackContext) -> bool:
    if not FORCE_SUB_ENABLED:
        return True

    user_id = update.effective_user.id
    chat_id = update.effective_chat.id

    # Load force sub channels from JSON
    try:
        with open(FORCE_SUB_FILE, 'r') as f:
            force_sub_channels = json.load(f)
    except FileNotFoundError:
        force_sub_channels = []

    if not force_sub_channels:
        return True

    # Check if user is a member of all required channels
    not_joined_channels = []
    for channel in force_sub_channels:
        try:
            member = await context.bot.get_chat_member(chat_id=channel, user_id=user_id)
            if member.status not in ["member", "administrator", "creator"]:
                not_joined_channels.append(channel)
        except Exception as e:
            not_joined_channels.append(channel)

    if not_joined_channels:
        # Create buttons for channels the user needs to join
        keyboard = [[InlineKeyboardButton(to_small_caps(f"Join {channel}"), url=f"https://t.me/{channel[1:]}")] for channel in not_joined_channels]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Send force sub message
        message = to_small_caps(f"Hey, {update.effective_user.first_name}\n\nYou haven't joined {len(not_joined_channels)}/{len(force_sub_channels)} channels yet.\nPlease join the channels provided below, then try again..!")
        await context.bot.send_message(
            chat_id=chat_id,
            text=message,
            reply_markup=reply_markup,
            parse_mode="HTML"
        )
        return False

    return True
