# config/config.py

# Bot Token (Replace with your actual bot token from BotFather)
BOT_TOKEN = "your-bot-token-here"

# Admin IDs (Add your Telegram user ID here)
ADMIN_IDS = [123456789]  # Example admin ID

# Default Welcome Message (Can be changed by admins)
DEFAULT_WELCOME_MESSAGE = "ʜᴇʏ, ~\n\nɪ ᴀᴍ ᴀɴ ᴀᴅᴠᴀɴᴄᴇ ꜰɪʟᴇ ꜱʜᴀʀᴇ ʙᴏᴛ ᴠ3.\n\nᴛʜᴇ ʙᴇꜱᴛ ᴘᴀʀᴛ ɪꜱ ɪ ᴀᴍ ᴀʟꜱᴏ ꜱᴜᴘᴘᴏʀᴛ ʀᴇQᴜᴇꜱᴛ ꜰᴏʀᴄᴇꜱᴜʙ ꜰᴇᴀᴛᴜʀᴇ, ᴛᴏ ᴋɴᴏᴡ ᴅᴇᴛᴀɪʟᴇᴅ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴄʟɪᴄᴋ"

# Paths to image directories
WELCOME_IMAGE_DIR = "images/welcome/"
ABOUT_IMAGE_DIR = "images/about/"
SETTINGS_IMAGE_DIR = "images/settings/"

# Force Subscription Settings
FORCE_SUB_ENABLED = True

# Database file for force subscription channels
FORCE_SUB_FILE = "config/force_sub_channels.json"

# Bot settings (for settings message)
SETTINGS = {
    "total_force_sub_channel": 2,
    "total_admins": 1,
    "total_banned_users": 0,
    "auto_delete_mode": "ENABLED",
    "protect_content": "DISABLED",
    "hide_caption": "ENABLED",
    "channel_button": "ENABLED",
    "request_fsub_mode": "ENABLED"
}
