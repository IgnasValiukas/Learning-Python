# Turime logo su peršviečiamu fonu, dydis 128*128.
# Atsisiųskite, ir perdarykite taip, kad nuo viršaus ir apačios nusiimtų po 28 eilutes pikselių.
# Išsisaugokite, nes naudosime sekančioms užduotims.

from PIL import Image

im = Image.open("logo_128.png")
#  (x1, y1, x2, y2)
box = (0, 28, 128, 100)
cropped_image = im.crop(box)
cropped_image.save('cropped_logo.png')

