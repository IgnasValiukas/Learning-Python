# sukurkite funkciją, kuri priimtų
# paveikslėlį
# kontrasto, spalvingumo, aštrumo ir ryškumo reikšmes
# išsaugoti ar ne reikšmę
# ir atitinkamai pakoreguotų paveikslėlio nustatymus.
# Parodytų nuotrauką ekrane.
# Priklausomai nuo pasirinkimo, išsaugotų arba ne.
# Išsaugokite faile,
# prie originalaus pavadinimo pridėję pvz. '_modified', tarkime dog_modified.jpg.

import urllib.request
from PIL import Image, ImageEnhance

url = "https://assets1.ignimgs.com/thumbs/userUploaded/2017/5/22/1200-1495500094872.jpg"
urllib.request.urlretrieve(url, "samurai_jack.jpg")


def image_editor(given_image, given_contrast, given_color, given_sharpness, given_brightness):
    im = Image.open(given_image)
    if given_contrast != 0:
        im = ImageEnhance.Contrast(im).enhance(given_contrast)
    im = ImageEnhance.Color(im).enhance(given_color)
    im = ImageEnhance.Sharpness(im).enhance(given_sharpness)
    if given_brightness >= 1:
        im = ImageEnhance.Brightness(im).enhance(given_brightness)
    im.show()
    save_image_input = input("Do you want to save image? (y/n): ")
    if save_image_input.lower() == 'y':
        new_image = given_image.replace(".", "_modified.")
        im.save(new_image)
    else:
        print("Image was not saved!")


contrast_value = float(input("Contrast value: "))
color_value = float(input("Color value: "))
sharpness_value = float(input("Sharpness value: "))
brightness_value = float(input("Brightness value: "))

save_values_input = input("Do you want to save values? (y/n): ")
if save_values_input.lower() == 'y':
    image_editor("samurai_jack.jpg", contrast_value, color_value, sharpness_value, brightness_value)
