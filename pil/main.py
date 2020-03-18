# https://code-maven.com/create-images-with-python-pil-pillow
# https://www.linuxidc.com/Linux/2019-04/158178.htm 换源

# example 1
# from PIL import Image
 
# img = Image.new('RGB', (60, 30), color = 'red')
# img.save('pil_red.png')


# example 2
# from PIL import Image, ImageDraw
 
# img = Image.new('RGB', (100, 30), color = (73, 109, 137))
 
# d = ImageDraw.Draw(img)
# d.text((10,10), "中国", fill=(255,255,0))
 
# img.save('pil_text.png')


# coding:utf-8

# from PIL import Image, ImageDraw, ImageFont

# image= Image.new('RGB', (559, 320),(255,255,255))
# draw = ImageDraw.Draw(image)

# # draw.text()
# # font = ImageFont.truetype("simsun.ttc", 40, encoding="unic")  # 设置字体
# draw.text((100, 50), "哈哈哈", 'black')
# # del draw
# img.save('pil_text.png')
# image.show()
# printers = win32print.EnumPrinters(10)
# print printers



from PIL import Image, ImageDraw, ImageFont, ImageFilter

#configuration
font_size=36
width=500
height=100
back_ground_color=('black')
font_size=36
font_color=('white')
unicode_text = "中文"

im  =  Image.new ( "RGB", (width,height), back_ground_color )
draw  =  ImageDraw.Draw ( im )
unicode_font = ImageFont.truetype("/mnt/c/Windows/Fonts/YuGothB.ttc", font_size, encoding="unic")
draw.text ( (10,10), unicode_text, font=unicode_font, fill=font_color )

im.save("text.jpg")


