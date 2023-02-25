import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Set up config
TOKEN = 'YOUR_TOKEN_HERE'
GROUP_LINK = 'YOUR_GROUP_LINK_HERE'
CHANNEL_LINK = 'YOUR_CHANNEL_LINK_HERE'
PLANS = {
    'Plan 1': '100 USD',
    'Plan 2': '200 USD',
    'Plan 3': '300 USD',
    'Plan 4': '400 USD',
    'Plan 5': '500 USD'
}

# Define the start command handler
def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Group", url=GROUP_LINK), InlineKeyboardButton("Channel", url=CHANNEL_LINK)],
        [InlineKeyboardButton("Donation", callback_data='donation')],
        [InlineKeyboardButton("Plans", callback_data='plans')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Welcome to the group info bot!', reply_markup=reply_markup)

# Define the callback query handler for the donation button
def donation_callback_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("Donate with PayPal", url='https://www.paypal.com')],
        [InlineKeyboardButton("Donate with Bitcoin", url='https://www.bitcoin.org')],
        [InlineKeyboardButton("Donate with Ethereum", url='https://www.ethereum.org')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text('Thank you for your interest in donating!', reply_markup=reply_markup)

# Define the callback query handler for the plans button
def plans_callback_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    message = 'Choose your plan:'
    for plan, price in PLANS.items():
        message += f'\n\n{plan}: {price}'
    query.edit_message_text(message)

# Define the group command handler
def group(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Join our group here: {GROUP_LINK}')

# Define the channel command handler
def channel(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Join our channel here: {CHANNEL_LINK}')

# Define the broadcast command handler
def broadcast(update: Update, context: CallbackContext) -> None:
    message = update.message.text[11:]
    for member in context.bot.get_chat_members(update.message.chat_id):
        if member.user.is_bot:
            continue
        try:
            context.bot.send_message(chat_id=member.user.id, text=message, parse_mode=ParseMode.HTML)
        except:
            pass

# Set up the main function
def main() -> None:
    # Set up the updater and dispatcher
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Add command handlers
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('group', group))
    dispatcher.add_handler(CommandHandler('channel', channel))
    dispatcher.add_handler(CommandHandler('broadcast', broadcast))

    # Add callback query handlers
    dispatcher.add_handler(CallbackQueryHandler(donation_callback_handler, pattern='donation'))
    dispatcher.add_handler(CallbackQueryHandler(plans_callback_handler, pattern='plans'))

   
