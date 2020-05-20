#!../venv/Scripts/python

# Creado por Jesus Imitola
# GitHub User: jgimitola

from telegram.ext import CommandHandler, CallbackQueryHandler, Updater

import config
import parserStars
import parserConstellations
from bot import *


# Generamos los archivos e imágenes.
def generate_files():
    parserStars.parse()
    parserConstellations.parse()
    from plotSky import plot
    plot()


def main():
    generate_files()  # Generamos archivos necesarios cada vez que se ejecute el bot.
    updater = Updater(token=config.TOKEN, use_context=True)

    # Configuramos todos los Handlers de comandos y botones.
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
    updater.dispatcher.add_handler(CallbackQueryHandler(send_stars, pattern='stars'))
    updater.dispatcher.add_handler(CallbackQueryHandler(send_fullsky, pattern='sky'))
    updater.dispatcher.add_handler(CallbackQueryHandler(constellations_menu, pattern='const'))
    updater.dispatcher.add_handler(CallbackQueryHandler(choose_constellation))

    # Escuchamos por peticiones.
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
