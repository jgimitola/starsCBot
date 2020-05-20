#!../venv/Scripts/python

# Creado por Jesus Imitola
# GitHub User: jgimitola

import json


def parse():
    stars = {}

    # Creamos un nuevo archivo estructurando la información.
    with open('./src/stars-rp/stars.txt') as fp:
        line = fp.readline()
        while line:
            params = line.strip().split(" ", 6)

            # Obtenemos todos los parametros.
            hdID = params[3]
            hrID = params[5]
            x = float(params[0])
            y = float(params[1])
            brillo = float(params[4])
            nombres = []
            if len(params) > 6:
                nombresTemp = params[6].split(";")
                for i in range(0, len(nombresTemp)):
                    nombres.append(nombresTemp[i].strip())
            else:
                nombres.append("UNNAMED")

            # Guadamos en el diccionario.
            stars[hdID] = {
                'hrID': hrID,
                'x': x,
                'y': y,
                'brillo': brillo,
                'nombres': nombres
            }
            line = fp.readline()

    # Guardamos el diccionario como .json
    with open("./src/stars-rp/stars.json", "w") as write_file:
        json.dump(stars, write_file)
