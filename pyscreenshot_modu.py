import pyscreenshot as p # pyright: ignore[reportMissingImports]
img=p.grab()
img.save("full_screeenshot.png")
img.show()
print("saved full_screeenshot.png")

#capture a specific region:
#define bounding box (left_x,top_y,right_x,bottom_y)
bbox=(100,100,500,400)
#grab region and save:
img=p.grab(bbox=bbox)
img.save("region_screenshot.png")
print("Saved region_screenshot.png")
img.show()