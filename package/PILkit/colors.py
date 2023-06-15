from PIL import Image

def with_transparent_bg(image: Image.Image):
    data = image.convert("RGBA").getdata()
    newData = []

    for item in data:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    image.putdata(newData)