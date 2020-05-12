import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler

updater = Updater(token='1241079844:AAF2wFu2HyJoI0VINKQcCBTQxwErgiV3FVY', use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
