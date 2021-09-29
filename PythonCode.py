from PIL import Image, ImageDraw,ImageFont
import sys

def Text_to_image(str1,str2,str3,str4,str5,str6):
    img =Image.open('overhead-view-white-daisy-flowers-baby-s-breath-petals-arranged-pink-background.jpg')
    fnt1=ImageFont.truetype('C:\Users\horizon\Desktop\Zain's Python Code\Font BebasNeue', 280)
    fnt = ImageFont.truetype('E:\Oswald/Oswald-VariableFont_wght.ttf', 180)
    d=ImageDraw.Draw(img)
    d.text((2000, 800), 'Results', font=fnt1,fill='yellow',align='center')
    d.text((1300,1100),str1,font=fnt)
    d.text((1300,1400),str2,font=fnt)
    d.text((1300, 1700), str3, font=fnt)
    d.text((1300, 2000), str4, font=fnt)
    d.text((1300, 2300), str5, font=fnt)
    d.text((1300, 2600), str6, font=fnt)
    img.save('Text.jpg')







Text_to_image('text 1','text 2','text 3','text 4','text 5','text 6')