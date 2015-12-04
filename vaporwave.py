# -*- coding: utf-8 -*-
# vaporwavor

from PIL import Image
import PIL
import time
import sys
import random
from PIL import ImageFont
from PIL import ImageDraw
import os

def terminalLine(string):
    sys.stdout.write(">")
    speed = 0.01
    for char in string:
        time.sleep(0.01)
        sys.stdout.write(char)
    print ""

def getmemeword():
    memewords = [
        u"ＡＥＳＴＨＥＴＩＣ",
        u"４２０//ＤＶＤ",
        u"ＳＴＯＩＣ",
        u"町で新しいミームマシンがあります",
        u"神様がありません",
        u"悲しい少年２０１５😢",
        u"コンピューター",
        u"パソコンが最も大切なもの",
        u"自分自身を殺す",
        u"ください",
        u"４２０ミームをブレーズ",
        u"ＭＡＣプラス",
        u"ミームを作ります。ドリームを壊しています",
        u"ＶＡＰＯＲＷＡＶＥが生活です",
        u"神様の思考を聞けます",
        u"１９８ＸＡＤミーム",
        u"像",
        u"愛",
        u"死",
        u"ミームは生活より大切",
        u"ミーム",
        u"私はコードです",
        u"俺はあなたを忘れた",
        u"私を助けて",
        u"神",
        u"お前の頭の中ですべてです",
        ]
    return memewords[random.randint(0, len(memewords)-1)]


def addFilter(pixel, r, g, b):
    arr = []
    arr.append(pixel[0] + 100)
    arr.append(0)
    arr.append(pixel[0] + 20)
    return tuple(arr)

def addBckgrndOverlay(im):
    # Get a random background image
    overlayImage = Image.open(getRandomImgFromPath("backgrounds"))
    # Convert it to RGB for compatibility
    overlayImage = overlayImage.convert('RGB')
    # Resize the image to be the same size as im, needed for Image.blend
    overlayImage = overlayImage.resize(im.size)

    # Blend the images together
    im = Image.blend(im, overlayImage, 0.5)

    return im

def drawMemeText(size, text, x, y, im):
    draw = ImageDraw.Draw(im)
    r = random.randint(0, 255)
    g = random.randint(0, 8)
    b = random.randint(0, 255)
    font=ImageFont.truetype("meiryob.ttc",size)
    draw.text((x+3, y+3),text, (r/2,g/2,b/2),font=font)
    draw.text((x, y),text,(r,g,b),font=font)
    return im

def addText(im):
    for i in range(random.randint(4, 10)):
        im = drawMemeText(random.randint(10, 100), getmemeword(),
                     random.randint(0, im.size[0]), random.randint(0, im.size[1]),
                     im)
    return im

def resize(im, factor):
    im = im.resize((int(im.size[0]/factor),int(im.size[1]/factor)))
    return im

def overlayImage(im, path):
    foreground = Image.open(path)
    foreground = foreground.convert('RGBA')
    foreground = resize(foreground, random.randint(1, 3))
    im.paste(foreground, (random.randint(0, im.size[0]), random.randint(0, im.size[1])), mask=foreground)
    return im

def addImg(im):
    for i in range(random.randint(3, 10)):
        newImgPath = getRandomImgFromPath("img")
        im = overlayImage(im, newImgPath)
    return im

def getRandomImgFromPath(path):
    if not os.path.isdir(path):
        return

    if not path.endswith("/"):
        path += "/"

    return path + random.choice(os.listdir(path))


def vaporwaveImage(path):
    terminalLine(u"ミームマシンをイニシャライズする…")
    im = Image.open(path)
    im = im.convert('RGB')
    pixels = im.load()
    terminalLine(u"ミームマシンを実行してる…")
    terminalLine(u"ＳＴＯＩＣのフィルターをやっています。待ってをください…")

    # You can put this part back in if you want
    """for i in range(im.size[0]): # width
        for j in range(im.size[1]): # height
            curr = pixels[i, j]
            pixels[i, j] = addFilter(pixels[i, j], random.randint(30, 100), 0, random.randint(0, 30))"""
    terminalLine(u"ＶＡＰＯＲＷＡＶＥの画像する、待ってをください…")
    im = addBckgrndOverlay(im)
    im = addImg(im)
    terminalLine(u"今、ＶＡＰＯＲＷＡＶＥのミームの文章する。待ってをください…")
    im = addText(im)
    im.show()






def main():
    fp = "mem.jpg"
    vaporwaveImage(fp)

if __name__ == "__main__":
    main()
