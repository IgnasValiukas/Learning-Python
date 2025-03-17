# parašykite programą, kuri nuskaitys failo turinį ir performuos jį
# Išsaugokite rezultatą į .json failą savo kompiuteryje.
import json

with open('json_colors.json', 'r') as file:
    data = json.load(file)

new_format = []
for color in data['colors']:
    color_hex = color['code']['hex']
    color_rgb = color['code']['rgba'][:3]

    new_format.append({
            "color": color["color"],
            "rgb": f"{color_rgb[0]}, {color_rgb[1]}, {color_rgb[2]}",
            "hex": color_hex
        })

new_data = {"colors": new_format}
print(new_data)
with open('new_colors.json', 'w') as file:
    json.dump(new_data, file, indent=2)

