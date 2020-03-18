import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

UNIT_SIZE = 768#高
TARGET_WIDTH = 1184*6 # 拼接完后的横向长度

path = '/mnt/c/Users/13823/Documents/leidian/Pictures/english/'


def createLeft (height, width) :
    font_size=36
    back_ground_color=('black')
    font_size=36
    font_color=('white')
    unicode_text = "中文"
    im  =  Image.new ( "RGB", (width,height), back_ground_color )
    draw  =  ImageDraw.Draw ( im )
    unicode_font = ImageFont.truetype("/mnt/c/Windows/Fonts/YuGothB.ttc", font_size, encoding="unic")
    draw.text ( (10,10), unicode_text, font=unicode_font, fill=font_color )
    return im


images = [] # 先存储所有的图像的名称
for root, dirs, files in os.walk(path):     
    for f in files :
        images.append(f)
for i in range(len(images)): 
    imagefile = []
    imagefile.append(Image.open(path+images[i])) 
    for image in imagefile:
        width, height = image.size
        print(width, height)
        info = createLeft(height, 200)
        target = Image.new('RGB', (200+width, height))    
        target.paste(info, (0, 0, 200, height))# 将复制到target的指定位置中
        target.paste(image, (200, 0, 200+width, height))# 将image复制到target的指定位置中
        quality_value = 100 # quality来指定生成图片的质量，范围是0～100
        target.save(images[i])