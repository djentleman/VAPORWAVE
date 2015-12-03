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

def addFilter(pixel):
    arr = []
    for i in range(3):
        arr.append(pixel[i] + random.randint(75, 255))
        if arr[i] > 255: arr[i] = 255
    return tuple(arr)

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
    draw = ImageDraw.Draw(im)
    font=ImageFont.truetype("meiryob.ttc",14)
    draw.text((10, 10),u"ＶＡＰＯＲＷＡＶＥ",(100,0,100),font=font)
    draw.text((8, 8),u"ＶＡＰＯＲＷＡＶＥ",(255,0,255),font=font)
    im.show()
    
    
    
    
    


def main():
    fp = "mem.jpg"
    vaporwaveImage(fp)

if __name__ == "__main__":
    main()
