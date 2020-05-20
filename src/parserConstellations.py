# !../venv/Scripts/python

# Creado por Jesus Imitola
# GitHub User: jgimitola

import os
import json


def parse():
    stars_dict = None
    with open('./src/stars-rp/stars.json') as fileJSON:
        stars_dict = json.load(fileJSON)  # Carga stars.json para hacer consultas.

    def getID(name):  # Busca en stars.json el ID asociado al nombre.
        for key in stars_dict:
            for nombre in stars_dict[key]['nombres']:
                if nombre == name:
                    return key
        return -1

    # Cargamos las constelaciones y creamos .json
    for filename in os.listdir('./src/constellations-raw'):
        constellation = {
            'lines': []
        }
        with open('./src/constellations-raw/' + filename) as f:
            line = f.readline()
            while line:
                name_pair = line.split(',')
                constellation['lines'].append((getID(name_pair[0]), getID(name_pair[1].strip())))
                line = f.readline()

        with open("./src/constellations-parsed/%s.json" % filename.strip('.txt'), "w") as write_file:
            json.dump(constellation, write_file)
