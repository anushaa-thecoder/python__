from PIL import Image, ImageFilter, ImageEnhance, ImageDraw,ImageOps,ImageFont  #pyright: ignore[reportMissingImports]
# inp=input("enter a text:")
i=Image.open("C:\\Users\\DEll\\OneDrive\\Pictures\\Screenshots 1\\Screenshot 2025-06-06 000452.png")
# i.show()
# i.save("PIL.png")

# #Image properties:
# print(i.format)
# print("size od image:",i.size)
# print("mode of file:",i.mode)
# print(i.filename)

# #Create a new image:
# img=Image.new("RGB",(200,200),"pink")
# img.show()

# #Rotate:
# a=i.rotate(angle=47,expand=True,fillcolor="pink")
# a.show()

# #resize:
# resized=i.resize((30,300))
# resized.show()

# #crop:
# crop=i.crop((50,50,200,200))
# crop.show()

# #convert color modes
# #convert the image to grayscale (L mode)
# gray=i.convert("L")
# gray.show()

# #convert the image to RGBA mode (adds alpha channel)
# rgba=i.convert("RGBA")
# rgba.show()

# #image filter effects:
# blurred=i.filter(ImageFilter.BLUR)
# blurred.show()

# sharp=i.filter(ImageFilter.SHARPEN)
# sharp.show()

# edges=i.filter(ImageFilter.FIND_EDGES)
# edges.show()

# #Image Enhancements:
# #Brightness
# enhancer=ImageEnhance.Brightness(i)
# bright_img=enhancer.enhance(0.5)
# bright_img.show()

# #contrast
# contrast=ImageEnhance.Contrast(i).enhance(1.8)
# contrast.show()

# #Sharpness
# sharp=ImageEnhance.Sharpness(i).enhance(3.0)
# sharp.show()

# #color
# color=ImageEnhance.Color(i).enhance(2.0)
# color.show()

#Drawing on image:
# draw=ImageDraw.Draw(i)

# #reactangle:
# draw.rectangle([40,40,80,80],fill="pink",outline="green",width=3)
# i.show()

# #ellipse
# draw.ellipse([220,50,350,200],fill="pink",outline="blue")
# i.show()

# #line
# draw.line((400,60,600,60),fill="red",width=4)
# i.show()

# Text
# font = ImageFont.load_default()
# #customised font:
# #font=ImageFont.truetype("arial.ttf",30)
# draw.text((400, 200), "Hello PIL!", fill="red", font=font)
# i.show()

#  Flip and Mirror 
# flipped = ImageOps.flip(i)  # Vertical flip
# flipped.show()

# mirrored = ImageOps.mirror(i)  # Horizontal flip
# mirrored.show()


# Paste One Image onto Another 
# Create new blank canvas
# canvas = Image.new("RGBA", (800, 600), "pink")
# canvas.show()
# # Paste original image onto canvas
# canvas.paste(i, (100, 50))  # Paste at x=100, y=100
# canvas.show()



# canvas = Image.new("RGBA", (i.width, i.height), "pink")
# canvas.show()
# rgba=i.convert("RGBA")
# canvas.paste(i, (100, 50))  # Paste at x=100, y=100
# canvas.show()
# save=Image.alpha_composite(i,canvas)
# save.show()

#transferency:
i2=Image.open("C:\\Users\\DEll\\OneDrive\\Pictures\\Screenshots 1\\Screenshot 2025-03-15 183532.png")
rgba=i.convert("RGBA")
rgba2=i2.convert("RGBA")
o=rgba2.resize((rgba.width,rgba.height))
save=Image.alpha_composite(rgba,o)
save.show()


