# !../venv/Scripts/python

import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def start(update, context):
    update.message.reply_text('¡Bienvenido, miremos al infinito y más allá!\nEscoge una opción para continuar.',
                              reply_markup=main_menu_keyboard())


def main_menu(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text='Escoje una opción.',
        reply_markup=main_menu_keyboard())


def constellations_menu(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text='Escoge una constelación.',
        reply_markup=constellations_menu_keyboard())


def choose_constellation(update, context):
    query = update.callback_query
    chat_id = update.callback_query.message.chat.id
    img = open('./src/imgs/%s-constellation.jpg' % query.data, 'rb')
    update.callback_query.message.reply_text('Mostrando ' + query.data)
    context.bot.send_photo(chat_id, photo=img)
    update.callback_query.message.reply_text(
        '¿Quieres ver otra constelación?',
        reply_markup=constellations_menu_keyboard())


def main_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Ver las estrellas', callback_data='stars')],
                [InlineKeyboardButton('Ver el cielo completo', callback_data='sky')],
                [InlineKeyboardButton('Ver constelaciones', callback_data='const')]]
    return InlineKeyboardMarkup(keyboard)


def constellations_menu_keyboard():
    keyboard = []
    for filename in os.listdir('./src/constellations-parsed'):
        name = filename.split('.json')[0]
        keyboard.append([InlineKeyboardButton(name, callback_data=name)])
    keyboard.append([InlineKeyboardButton('Volver', callback_data='main')])
    return InlineKeyboardMarkup(keyboard)


def send_stars(update, context):
    chat_id = update.callback_query.message.chat.id
    img = open('./src/imgs/sky.jpg', 'rb')
    context.bot.send_photo(chat_id, photo=img)


def send_fullsky(update, context):
    chat_id = update.callback_query.message.chat.id
    img = open('./src/imgs/full-sky.jpg', 'rb')
    context.bot.send_photo(chat_id, photo=img)
