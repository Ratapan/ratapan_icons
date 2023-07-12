import os
import re

COLORS = ['#a07250', '#dca780', '#e3c4ad']
COLORSUPER = ['#A07250', '#DCA780', '#E3C4AD']
VARS = ['var(--color-a)', 'var(--color-b)', 'var(--color-c)']

NEW_ICONS_FOLDER = 'color_vars'
ICONS_FOLDER = 'coffe'

HERE_PATH = os.getcwd()
def FILE_PATH(a): return HERE_PATH+'\\'+ICONS_FOLDER+'\\'+a
def NEW_FILE_PATH(a): return HERE_PATH+'\\'+NEW_ICONS_FOLDER+'\\'+a


try:
    os.mkdir(NEW_ICONS_FOLDER)
except:
    print('ya existe la carpeta')

def is_svg(name):
    final = name[-3:]
    if final == 'svg':
        return name
    return ''


files_names = list(map(is_svg, os.listdir(ICONS_FOLDER)))
files = []

for i, item in enumerate(files_names):
    if item != '':
        pre_file = open(HERE_PATH+'\\'+ICONS_FOLDER+'\\'+item, "r").read()
        newFile = pre_file
        for index in range(len(COLORS)):
            newFile = re.sub(COLORS[index], VARS[index], newFile)
            newFile = re.sub(COLORSUPER[index], VARS[index], newFile)

        files.append({'name': item ,'text':newFile})

for i, item in enumerate(files):
    print('nuevo => ', item['name'])
    newSvg = open(HERE_PATH+'\\'+ NEW_ICONS_FOLDER +'\\'+item['name'], "w")
    newSvg.write(item['text'])
    newSvg.close()