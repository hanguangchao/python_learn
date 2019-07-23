# -*-coding:utf-8-*-

import pytesseract
import sys

from PIL import Image

im = Image.open(sys.argv[1])
im = im.convert('L')

def initTable(threshold=140):
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    return table

binaryImage = im.point(initTable(), '1')
binaryImage.show()
print(pytesseract.image_to_string(binaryImage, config='-psm 7'))
