from PIL import Image, ImageFont, ImageDraw, ImageFilter
import random


def genVerifiCode():
    def rndColor():
        return random.randint(34, 255), random.randint(34, 255), random.randint(34, 255)

    def rndColor2():
        return random.randint(40, 137), random.randint(40, 137), random.randint(40, 137)

    def rndChar():
        return chr(random.randint(65, 90))

    w = 60 * 4
    h = 60
    # 获取一个lmage对象,参数分别是RGBf=模式。宽，高，颜色
    image = Image.new('RGB', (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    for x in range(w):
        for y in range(h):
            draw.point((x, y), fill=rndColor())
    font = ImageFont.truetype('cambria.ttc', 36)
    for t in range(4):
        draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
    image = image.filter(ImageFilter.BLUR)
    return image
    # 保存到硬盘,名为code.jpg格式为jpeg的图片
    # image.save('code.jpg', 'jpeg')


