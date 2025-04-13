# utils/message_cleaner.py

async def delete_message(context, chat_id, message_id):
    """
    Delete a message in the chat.
    """
    try:
        await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
    except Exception as e:
        print(f"Error deleting message: {e}")
