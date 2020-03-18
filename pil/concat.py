import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path

path = '/mnt/c/Users/13823/Documents/leidian/Pictures/'


def createLeft (height, width, otherText) :
    font_size=36
    back_ground_color=('black')
    font_size=36
    font_color=('white')
    unicode_text = "中文"
    im  =  Image.new ( "RGB", (width,height), back_ground_color )
    draw  =  ImageDraw.Draw ( im )
    unicode_font = ImageFont.truetype("/mnt/c/Windows/Fonts/AdobeKaitiStd-Regular.otf", font_size, encoding="unic")
    texts = ['超清', '蓝光', '1080p', '云盘发货', '拍下即发', '无广告', otherText if otherText else '']
    height = 10
    lineHeight = 80
    for text in texts: 
        draw.text ( (30,height), text, font=unicode_font, fill=font_color )
        height +=lineHeight
    return im


def deal_with_images(path, otherText):
    images = [] # 先存储所有的图像的名称
    INFO_WIDTH = 200 
    RESULT = 'result'
    if not os.path.exists(path):
        return
    for file in os.listdir(path):     
        if file != RESULT:
            images.append(file)
    for i in range(len(images)): 
        imagefile = []
        imagefile.append(Image.open(path+images[i])) 
        for image in imagefile:
            width, height = image.size
            info = createLeft(height, INFO_WIDTH, otherText)
            target = Image.new('RGB', (INFO_WIDTH+width, height))    
            target.paste(info, (0, 0, INFO_WIDTH, height))# 将复制到target的指定位置中
            target.paste(image, (INFO_WIDTH, 0, INFO_WIDTH+width, height))# 将image复制到target的指定位置中
            quality_value = 100 # quality来指定生成图片的质量，范围是0～100
            # print(Path(path + 'result/'+images[i]))
            # print(type Path(path + 'result/'))
            target_path = path + RESULT
            if not os.path.exists(target_path):
                os.mkdir(target_path)
            target.save(os.path.join(target_path,  images[i]))


languages = ['english', 'chinese','cantonese', 'japanese', 'korean', 'others']
lang_to_text = {'english': '英语中字', 'chinese': '国语中字','cantonese':'粤语中字', 'japanese': '日语中字', 'korean':'韩语中字', 'others': None}

for language in languages:
    deal_with_images(path+language+'/', lang_to_text.get(language)) 
