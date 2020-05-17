#!../venv/Scripts/python

import json


def parse():
    stars = {}

    with open('./src/stars-rp/stars.txt') as fp:
        line = fp.readline()
        while line:
            params = line.strip().split(" ", 6)
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

            stars[hdID] = {
                'hrID': hrID,
                'x': x,
                'y': y,
                'brillo': brillo,
                'nombres': nombres
            }
            line = fp.readline()

    with open("./src/stars-rp/stars.json", "w") as write_file:
        json.dump(stars, write_file)
