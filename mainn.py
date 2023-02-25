import logging
import os

from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackContext

# Import config.py
from config import DONATE_STRING, HELP_IMG, GROUPSTART_IMG, PM_IMG

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define command handlers
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Hi {user.first_name}!\n\nWelcome to the group info bot. Use the /help command to see available commands.",
    )

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    help_text = f"""*Available commands:*\n
- /start: Start the bot
- /help: Show this help message
- /donate: Donate to support the bot
- /plans: Show available plans
- /group: Show group info
- /channel: Show channel info
- /broadcast: Broadcast a message to all users (admins only)
"""
    context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=HELP_IMG,
        caption=help_text,
        parse_mode=ParseMode.MARKDOWN,
    )

def donate(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /donate is issued."""
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Thank you for considering donating to support the bot!\n\n{DONATE_STRING}",
        parse_mode=ParseMode.MARKDOWN,
    )

def plans(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /plans is issued."""
    context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=PM_IMG[0],
        caption="*Available Plans:*\n\n1. Plan 1\n2. Plan 2\n3. Plan 3\n4. Plan 4\n5. Plan 5",
        parse_mode=ParseMode.MARKDOWN,
    )

def group(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /group is issued."""
    context.bot.send_video(
        chat_id=update.effective_chat.id,
        video=GROUPSTART_IMG,
        caption="*Group Info:*\n\n- Group Name: Test Group\n- Group Description: This is a test group.",
        parse_mode=ParseMode.MARKDOWN,
    )

def channel(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /channel is issued."""
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="*Channel Info:*\n\n- Channel Name: Test Channel\n- Channel Description: This is a test channel.",
        parse_mode=ParseMode.MARKDOWN,
    )

def broadcast(update: Update, context: CallbackContext) -> None:
    """Broadcast a message to all users (admins only)."""
    user = update.effective_user
    if user.username == 'admin':
        message = "This is a broadcast message!"
        for chat_id in USER_INFO:
            try:
                context.bot.send_message(chat_id=chat_id, text=message)
            except Exception as e:
                logger.warning(f"Failed to send message to chat {chat_id}. Error: {e}")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="You're not authorized to use this command.")
