# http://random.cat/ kas kartą užkrauna vis skirtingą katės nuotrauką.
# Parašykite funkciją, kuriai į parametrus įrašius, kiek norime nuotraukų, išsaugotų jas mūsų kompiuteryje.
# image url example: https://purr.objects-us-east-1.dream.io/i/JL7FU.jpg

import requests
import re


def download_images(images_number):
    image_pattern = r'https://purr.objects-us-east-1.dream.io/i/(.+)\.(jpg|jpeg|png|gif)'
    for number in range(images_number):
        response = requests.get('http://random.cat/')

        image_match = re.search(image_pattern, response.text)

        if not image_match:
            print("Can't find image!")
            continue
        image_url = image_match.group(0)
        image_type = image_match.group(2)
        image_data = requests.get(image_url).content
        image_name = f'cat_{number + 1}.{image_type}'

        with open(image_name, 'wb') as file:
            file.write(image_data)

        print("Downloaded")


download_images(3)
