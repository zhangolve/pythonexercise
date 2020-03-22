import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path
import requests
from bunch import bunchify 

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


languages = ['english', 'chinese','cantonese', 'japanese', 'korean', 'french', 'others']
lang_to_text = {'english': '英语中字', 'chinese': '国语中字','cantonese':'粤语中字', 'japanese': '日语中字', 'korean':'韩语中字', 'french':'法语中字', 'others': None}
URL = 'http://api.douban.com/v2/movie/new_movies?apikey=0df993c66c0c636e29ecbb5344252a4a'


from types import SimpleNamespace

def dict2obj(data):
    """将字典对象转换为可访问的对象属性"""
    if not isinstance(data, dict):
        raise ValueError('data must be dict object.')

    def _d2o(d):
        _d = {}
        for key, item in d.items():
            if isinstance(item, dict):
                _d[key] = _d2o(item)
            else:
                _d[key] = item
        return SimpleNamespace(**_d)

    return _d2o(data)


for language in languages:
    deal_with_images(path+language+'/', lang_to_text.get(language)) 
    # pass

def request_download():
    import requests
    r = requests.get(IMAGE_URL)
    with open('./image/img2.png', 'wb') as f:
        f.write(r.content)


# def get_douban_new_movie():
#      headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
#      r = requests.get(URL, headers=headers)
#      result = dict2obj(r.json());
#      subjects = result.subjects
#      for sub in subjects:
#          sub = dict2obj(sub)
#          title = sub.title
#          print(title)

# get_douban_new_movie()


# files.read(path[, encoding = "utf-8"])
# path {string} 路径
# encoding {string} 字符编码，可选，默认为utf-8
# 返回 {string}
# 读取文本文件path的所有内容并返回。如果文件不存在，则抛出FileNotFoundException。

# log(files.read("/sdcard/1.txt"));

# 读取到需要的影片，从一个txt中。

