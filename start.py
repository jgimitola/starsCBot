#!../venv/Scripts/python

# Creado por Jesus Imitola
# GitHub User: jgimitola

import sys
import os

# Establecemos el directorio del proyecto.
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.extend([ROOT_DIR, ROOT_DIR + '\\src'])

# Ejecutamos el bot.
print("El bot se está ejecutando")
exec(open('./src/main.py').read())
