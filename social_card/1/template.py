import random, sys, os
import requests

from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps
from PILkit.circular import create_round_image, add_corners
from PILkit.colors import with_transparent_bg

def main(person_name, profile_image, data, metaline: str = "", background_color: str = "#3e4873",
         stroke=None, stroke_width: int = 8):
    lendata = len(data.keys())

    size = 150 + (150 // lendata)
    img = Image.new("RGB", (1500, 900 if lendata < 3 else size + (lendata * 80)), background_color)
    imgdraw = ImageDraw.ImageDraw(img)

    person_img = Image.open(profile_image).resize((size, size))
    person_img, _ = create_round_image(person_img)
    cwidth = (img.width // 2  - (person_img.width // 2))
    img.paste(person_img, (cwidth, 50), person_img)

    name_height = img.height - (img.height // 4) - (person_img.height // 4)
    if person_name:
        font = ImageFont.truetype("GOTHIC", size=30)
        imgdraw.text(((img.width // 3) + len(person_name) * 16, person_img.height + 60), person_name, font=font)

    if metaline:
        font = ImageFont.truetype("cour", size=20)
        if person_name:
            name_height += 70

        imgdraw.text((img.width // 2 - (person_img.width // 3), person_img.height + 105), metaline, font=font)
    
    current = 0
    font = ImageFont.truetype("comicbd", size=28)

    height = person_img.height + 150
    for iconId, username in data.items():
        path = f"assets/{iconId}.png"
        if not os.path.exists(path):
            req = requests.get(f"https://img.icons8.com/fluency/48/{iconId}.png")
            if req.headers["Content-Type"] == "application/json":
                print(iconId, "not found")
                path = "assets/globe.png"
            else:
                with open(path, "wb") as file:
                    file.write(req.content)
        current += 1

        icon = Image.open(path).resize((80, 80))

        if (current % 2 == 0):
            img.paste(icon, (int(img.width // 1.8), height - 40), icon)
            imgdraw.text((int(img.width // 1.8) + icon.width + 20, height - 40 + (icon.height // 3)), username, font=font)
        elif (current == lendata):
            height += 10
            img.paste(icon, ((img.width // 2 - int(person_img.width // 2) - len(username)*8, height)), icon)
            imgdraw.text((img.width // 2 - int(person_img.width // 1.5) + (len(username)*2) + 20, height + (icon.height // 3)), username, font=font)
        else:
            img.paste(icon, ((img.width // 5, height)), icon)
            imgdraw.text(((img.width // 5) + icon.width + 20, height + (icon.height // 3)), username, font=font)
        height += 45
    
    if stroke:
        img = ImageOps.expand(img, stroke_width, stroke)
    #     bullet = Image.open(bullet_path).resize((65, 65))
    #     height = int(img.height // 3.5)
    #     width = (person_img.width + 300)
    #     font = ImageFont.truetype("JOKERMAN", size=40)

    #     for line in bulletins:
    #         img.paste(bullet, (width, height), bullet)

    #         imgdraw.text((width+ bullet.width + 30, height), line, font=font)
    #         height += 80

    #  imgdraw = ImageDraw.ImageDraw(img)

    # text_font = ImageFont.truetype("fonts/SecularOne-Regular.ttf", size=45)
    # main_header = "Happy Birthday!"
    # imgdraw.text(((img.width // 3), person_img.height + 220), main_header, font=text_font, fill="black")

    #     background.paste(img, (border_size // 2, border_size // 2), img)
    #  background.save("output.png")
    #  background.show()
   # img.show()
    img.save("output.png")


main("Devesh Pal", "person.png", metaline="Developer", data={
    "telegram-app": "@KarbonCopy",
    "github": "@New-Dev0",
     "twitter": "NewDev0",
    "discord": "@KarbonCopy",
    "docker": "New-dev0",
    "facebook-messenger": "UnOccupied",
    "valorant": "@Krash25#855",
    }, background_color="#191f24", stroke="white", stroke_width=1)
