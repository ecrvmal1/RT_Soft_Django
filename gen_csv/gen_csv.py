import random
from PIL import Image, ImageDraw, ImageFont

categories = [
    "airport",
    "bike",
    "boat",
    "bridge",
    "bus",
    "car",
    "city",
    "flight",
    "highway",
    "hotel",
    "museum",
    "park",
    "parking",
    "pilot",
    "port",
    "road",
    "ship",
    "shop",
    "station",
    "street",
    "ticket",
    "tower",
    "train",
]


def draw_image(output_filename, x_size, y_size, img_text):
    image = Image.new("RGB", (x_size, y_size), (255, 255, 255))
    fnt = ImageFont.load_default()
    draw = ImageDraw.Draw(image)
    draw.multiline_text((5, 5), img_text, font=fnt, fill=(0, 0, 0))
    draw.rectangle((0, 0, x_size - 1, y_size - 1), outline="red", width=1)
    image.save(output_filename)
    print(f'Drawing {output_filename}')


def generate_csv():
    with open("input_data.csv", mode="w", encoding="utf-8") as out_file:
        for i in range(1, 10):
            filename = f'image{i}.jpg'
            need_shows = random.randint(1, 3000)
            category_list = random.sample(categories, random.randint(1, 10))
            category_text_img = "\n".join(category_list)
            category_text_csv = ";".join(category_list)
            print(category_text_img)
            print(category_text_csv)
            text_line = f'image{i}.jpg;{need_shows};{category_text_csv}\n'
            out_file.write(text_line)
            draw_image(
                filename,
                200,
                200,
                f'{filename}\n\n{category_text_img}')
            print(f'image image{i}.jpg was drown; ')


if __name__ == "__main__":
    generate_csv()
