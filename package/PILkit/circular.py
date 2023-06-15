# https://stackoverflow.com/questions/890051/how-do-i-generate-circular-thumbnails-with-pil

from PIL import ImageDraw

def create_round_image(image):
    from PIL import ImageDraw, Image

    bigsize = (image.size[0] * 3, image.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(image.size, Image.LANCZOS)
    image.putalpha(mask)
    return image, mask


def add_corners(im, rad):
    from PIL import Image, ImageDraw

    circle = Image.new("L", (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2 - 1, rad * 2 - 1), fill=255)
    alpha = Image.new("L", im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im


def draw_circle(draw: ImageDraw.ImageDraw, point, radius: int, fill="black"):
    x, y = point
    leftUpPoint = (x - radius, y - radius)
    rightDownPoint = (x + radius, y + radius)
    twoPointList = [*leftUpPoint, *rightDownPoint]
    draw.ellipse(twoPointList, fill=fill)
