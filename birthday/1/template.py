import random, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps
from PILkit.circular import create_round_image, add_corners, draw_circle


def get_random_color():
    return random.choice(["#c4d7f5", "#f5c4e8", "#f5e0c4", "#ccc5d6"])


def main(
    person_name,
    greeting,
    image_path,
    border_size=80,
    box_color="#c4d7f5",
    background_image: str = "assets/background.webp",
    mainHeading: str = "Happy Birthday"
):
    background = Image.open(background_image).resize((1000, 1000))
    img = Image.new("RGB", background.size, box_color)

    person_img = Image.open(image_path)
    person_img, mask = create_round_image(person_img)

    # FIX: circular with stroke
    person_img = ImageOps.expand(person_img, (20, 20, 20, 60), fill="white")
    person_img = ImageOps.expand(person_img, 2)
    img.paste(person_img, (300, 200))
    imgdraw = ImageDraw.ImageDraw(img)

    text_font = ImageFont.truetype("fonts/SecularOne-Regular.ttf", size=45)

    imgdraw.text(
        ((img.width // 3), person_img.height + 220),
        mainHeading,
        font=text_font,
        fill="black",
    )
    text_font.size = 80
    imgdraw.text(
        ((img.width // 3 + 50), person_img.height + 280),
        person_name,
        font=text_font,
        fill="teal",
    )

    img = img.resize((img.width - border_size, img.height - border_size))
    img = add_corners(img, 20)

    bgoverlay = Image.new("L", (img.width + 10, img.height + 10), int(255 * 0.2))
    background.paste(
        bgoverlay, (border_size // 2, border_size // 2), add_corners(bgoverlay, 20)
    )
    background.paste(img, (border_size // 2, border_size // 2), img)
    # bgdraw = ImageDraw.Draw(background)
    #  bgdraw.ellipse(((background.width // 2, background.height // 2), (210, 190)))

    background.save("output.png")


#    background.show()


main("Devesh Pal", "Wish you!", "person.png")
