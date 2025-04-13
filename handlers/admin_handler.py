# handlers/admin_handler.py

import json
from telegram import Update
from telegram.ext import CallbackContext
from config.config import ADMIN_IDS, FORCE_SUB_FILE
from utils.font_formatter import to_small_caps

async def force_sub(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id

    if user_id not in ADMIN_IDS:
        await context.bot.send_message(chat_id=chat_id, text=to_small_caps("You are not an admin!"))
        return

    # Load force sub channels
    try:
        with open(FORCE_SUB_FILE, 'r') as f:
            force_sub_channels = json.load(f)
    except FileNotFoundError:
        force_sub_channels = []

    if not force_sub_channels:
        await context.bot.send_message(chat_id=chat_id, text=to_small_caps("No force sub channels set!"))
        return

    channels_list = "\n".join([f"- {channel}" for channel in force_sub_channels])
    message = to_small_caps(f"Force Sub Channels:\n\n{channels_list}")
    await context.bot.send_message(chat_id=chat_id, text=message)

async def add_force_sub(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id

    if user_id not in ADMIN_IDS:
        await context.bot.send_message(chat_id=chat_id, text=to_small_caps("You are not an admin!"))
        return

    if not context.args:
        await context.bot.send_message(chat_id=chat_id, text=to_small_caps("Please provide a channel username! Example: /req_force_sub_add @channel"))
        return

    channel = context.args[0]
    if not channel.startswith("@"):
        channel = f"@{channel}"

    # Load current force sub channels
    try:
        with open(FORCE_SUB_FILE, 'r') as f:
            force_sub_channels = json.load(f)
    except FileNotFoundError:
        force_sub_channels = []

    if channel in force_sub_channels:
        await context.bot.send_message(chat_id=chat_id, text=to_small_caps(f"{channel} is already in the force sub list!"))
        return

    force_sub_channels.append(channel)
    with open(FORCE_SUB_FILE, 'w') as f:
        json.dump(force_sub_channels, f)

    await context.bot.send_message(chat_id=chat_id, text=to_small_caps(f"Added {channel} to force sub list!"))

async def remove_force_sub(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id

    if user_id not in ADMIN_IDS:
        await context.bot.send_message(chat_id=chat_id, text=to_small_caps("You are not an admin!"))
        return

    if not context.args:
        await context.bot.send_message(chat_id=chat_id, text=to_small_caps("Please provide a channel username! Example: /req_force_sub_remv @channel"))
        return

    channel = context.args[0]
    if not channel.startswith("@"):
        channel = f"@{channel}"

    # Load current force sub channels
    try:
        with open(FORCE_SUB_FILE, 'r') as f:
            force_sub_channels = json.load(f)
    except FileNotFoundError:
        force_sub_channels = []

    if channel not in force_sub_channels:
        await context.bot.send_message(chat_id=chat_id, text=to_small_caps(f"{channel} is not in the force sub list!"))
        return

    force_sub_channels.remove(channel)
    with open(FORCE_SUB_FILE, 'w') as f:
        json.dump(force_sub_channels, f)

    await context.bot.send_message(chat_id=chat_id, text=to_small_caps(f"Removed {channel} from force sub list!"))
