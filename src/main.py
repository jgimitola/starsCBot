#!../venv/Scripts/python

from telegram.ext import CommandHandler, CallbackQueryHandler, Updater

import config
import parserStars
import parserConstellations
import plotSky
from bot import *


def generate_files():
    parserStars.parse()
    parserConstellations.parse()
    plotSky.plot()


def main():
    generate_files()
    updater = Updater(token=config.TOKEN, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
    updater.dispatcher.add_handler(CallbackQueryHandler(send_stars, pattern='stars'))
    updater.dispatcher.add_handler(CallbackQueryHandler(send_fullsky, pattern='sky'))
    updater.dispatcher.add_handler(CallbackQueryHandler(constellations_menu, pattern='const'))
    updater.dispatcher.add_handler(CallbackQueryHandler(choose_constellation))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
