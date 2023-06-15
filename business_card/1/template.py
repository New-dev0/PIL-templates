import random, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps
from PILkit.circular import create_round_image, add_corners
from PILkit.colors import with_transparent_bg


def main(
    person_name,
    profile_image,
    bulletins: list = None,
    tag: str = "",
    background_color: str = "#3e4873",
    bullet_path="assets/bullet.png",
):
    img = Image.new("RGB", (1500, 1000), background_color)
    imgdraw = ImageDraw.ImageDraw(img)

    person_img = Image.open(profile_image)
    #    person_img, _ = create_round_image(person_img)

    person_img = add_corners(person_img, 60)
    img.paste(person_img, (160, img.height // 4), person_img)

    name_height = img.height - (img.height // 4) - (person_img.height // 4)
    if person_name:
        font = ImageFont.truetype("GOTHIC", size=30 if len(person_name) > 18 else 50)
        imgdraw.text((220, name_height), person_name, font=font)

    if tag:
        font = ImageFont.truetype("GOTHIC", size=30)
        if person_name:
            name_height += 70
        imgdraw.text((200 + person_img.width // 3, name_height), tag, font=font)

    if bulletins:
        bullet = Image.open(bullet_path).resize((65, 65))
        height = int(img.height // 3.5)
        width = person_img.width + 300
        font = ImageFont.truetype("JOKERMAN", size=40)

        for line in bulletins:
            img.paste(bullet, (width, height), bullet)

            imgdraw.text((width + bullet.width + 30, height), line, font=font)
            height += 80

    #  imgdraw = ImageDraw.ImageDraw(img)

    # text_font = ImageFont.truetype("fonts/SecularOne-Regular.ttf", size=45)
    # main_header = "Happy Birthday!"
    # imgdraw.text(((img.width // 3), person_img.height + 220), main_header, font=text_font, fill="black")

    #     background.paste(img, (border_size // 2, border_size // 2), img)
    #  background.save("output.png")
    #  background.show()
    #    img.show()
    img.save("output.png")


main(
    "Devesh Pal",
    "person.png",
    tag="Developer",
    bulletins=["55 Years Old", "Python", "Javascript", "Flutter", "Dart"],
)
