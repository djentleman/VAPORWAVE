# -*- coding: utf-8 -*-
# vaporwavor

from PIL import Image
import time
import sys
import random
from PIL import ImageFont
from PIL import ImageDraw 

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
        ]
    return memewords[random.randint(0, len(memewords)-1)]
    

def addFilter(pixel):
    arr = []
    for i in range(3):
        arr.append(pixel[i] + random.randint(75, 255))
        if arr[i] > 255: arr[i] = 255
    return tuple(arr)

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
    for i in range(random.randint(5, 30)):
        im = drawMemeText(random.randint(10, 100), getmemeword(),
                     random.randint(0, im.size[0]), random.randint(0, im.size[1]-100),
                     im)
    return im
                   
                   

def vaporwaveImage(path):
    terminalLine(u"ミームマシンをイニシャライズする…")
    im = Image.open(path)
    im = im.convert('RGB')
    pixels = im.load()
    terminalLine(u"ミームマシンを実行してる…")
    terminalLine(u"ＳＴＯＩＣのフィルターをやっています。待ってをください…")
    for i in range(im.size[0]): # width
        for j in range(im.size[1]): # height
            curr = pixels[i, j]
            pixels[i, j] = addFilter(pixels[i, j])
    terminalLine(u"今、ＶＡＰＯＲＷＡＶＥのミームの文章する。待ってをください…")
    im = addText(im)
    im.show()
    
    
    
    


def main():
    fp = "mem.jpg"
    vaporwaveImage(fp)

if __name__ == "__main__":
    main()
