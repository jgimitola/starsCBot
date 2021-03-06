# !../venv/Scripts/python

# Creado por Jesus Imitola
# GitHub User: jgimitola

import json
import os

from PIL import Image, ImageDraw

stars_dict = None
with open('./src/stars-rp/stars.json') as fileJSON:
    stars_dict = json.load(fileJSON)

size = 1000
scale = (size // 2)


# Dibuja las estrellas y permite modificacion.
def drawStars():
    im = Image.new('RGB', (size, size), (0, 0, 0))
    draw = ImageDraw.Draw(im)

    for id in stars_dict:
        x = round(scale * (1 + stars_dict[id]['x']))
        y = round(scale * (1 - stars_dict[id]['y']))
        tamaño_base_estrella = round(10.0 / (stars_dict[id]['brillo'] + 2))

        draw.rectangle((x - tamaño_base_estrella // 2, y - tamaño_base_estrella // 2, x + tamaño_base_estrella // 2,
                        y + tamaño_base_estrella // 2), fill=(255, 255, 255))

    return im


# Toma el dibujo de las estrellas y lo guarda.
def plotStars():
    im = drawStars()
    im.save('./src/imgs/sky.jpg')


# Dibuja una constelacion en especifica.
def drawConstellation(constellation_name, image):
    if image is None:
        im = drawStars()
    else:
        im = image
    draw = ImageDraw.Draw(im)

    constellation_dictionary = None
    with open('./src/constellations-parsed/%s' % constellation_name) as f:
        constellation_dictionary = json.load(f)

    for line in constellation_dictionary['lines']:
        point1 = stars_dict[line[0]]
        point2 = stars_dict[line[1]]
        x = round(scale * (1 + point1['x']))
        y = round(scale * (1 - point1['y']))
        x2 = round(scale * (1 + point2['x']))
        y2 = round(scale * (1 - point2['y']))
        draw.line((x, y, x2, y2), fill=(212, 255, 0), width=2)

    return im


# Toma la constelación y la guarda.
def plotConstellation(constellation_name, image=None, noSave=False):
    im = drawConstellation(constellation_name, image)
    if not noSave:
        im.save('./src/imgs/%s-constellation.jpg' % constellation_name.split('.json')[0])
    return im


# Genera todas las constelaciones individualmente.
def plotConstellations():
    for filename in os.listdir('./src/constellations-parsed'):
        if not filename.__contains__('.gitkeep'):
            plotConstellation(filename, None, False)


# Genera todas las constelaciones de manera única.
def plotSky():
    image_temp = None
    for filename in os.listdir('./src/constellations-parsed'):
        if not filename.__contains__('.gitkeep'):
            image_temp = plotConstellation(filename, image_temp, True)
    image_temp.save('./src/imgs/full-sky.jpg')


def plot():
    plotSky()
    plotStars()
    plotConstellations()
