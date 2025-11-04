#create an img with user defined text:
from PIL import Image, ImageFont,ImageDraw # pyright: ignore[reportMissingImports]
# inp=input("enter a text:")
# canvas = Image.new("RGBA", (400, 800), "pink")
# canvas.show()
# draw=ImageDraw.Draw(canvas)
# font = ImageFont.load_default()
# draw.text((100, 200),inp , fill="black", font=font)
# canvas.show()

#create a new image and add random code which contains alphanumeric character
# import random as r
# import string
# ch=''
# canvas = Image.new("RGBA", (400, 800), "black")
# canvas.show()
# re=string.ascii_letters+string.digits
# for i in range(6):
#     ch=ch+r.choice(re)
# font = ImageFont.load_default()
# draw=ImageDraw.Draw(canvas)
# draw.text((100, 200),ch , fill="white", font=font)
# canvas.show()


#add text at bottom of image(watermark types):
# import random as r
# import string
# ch=''
# canvas = Image.new("RGBA", (400, 800), "black")
# canvas.show()
# h,w=canvas.size
# print(h,w)
# re=string.ascii_letters+string.digits
# for i in range(6):
#     ch=ch+r.choice(re)
# font=ImageFont.truetype("arial.ttf",30)
# draw=ImageDraw.Draw(canvas)
# draw.text((h-50, w-50),ch , fill="white", font=font)
# canvas.show()

i2=Image.open("C:\\Users\\DEll\\OneDrive\\Pictures\\Screenshots 1\\Screenshot 2025-03-15 183532.png")
i2.convert("RGBA")
img=Image.new("RGBA",(i2.size),(255,255,255,0))
draw=ImageDraw.Draw(img)
font=ImageFont.truetype("arial.ttf",50)
draw.text((i2.width-400, i2.height-200), "Hello PIL!", fill="black", font=font)
save=Image.alpha_composite(i2,img)
save.show()

