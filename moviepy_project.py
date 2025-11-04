#create a python prog using moviepy that takes attleast 3 imgs and 1 audio filee as a input
#generate a slideshow video where each img is shown for 3 secs with bg music
#export the final vdo as slideshow.mp4 at 24fps
from moviepy.editor import* #type: ignore
clip1 = ImageClip("test.jpg") # type: ignore
clip1 = clip1.set_duration(3)
clip2 = ImageClip("anmuu.jpg") # type: ignore
clip2= clip2.set_duration(3)
clip3 = ImageClip(r"C:\Users\DEll\OneDrive\Pictures\Screenshots 1\Screenshot 2025-03-15 183532.png") # type: ignore
clip3 = clip3.set_duration(3)
v=concatenate_videoclips([clip1,clip2,clip3],method="compose")  # type: ignore
audio1 = AudioFileClip("extract.mp3")  # type: ignore
audioo=v.set_audio(audio1)
audioo.write_videofile("bgm.mp4",fps=24)


"""Create a python progs using movepy that takes 2 vdoclips as input 
display the before vdoclip and after vdoclip in layout
appply b&w effect to 2nd clipand add text label as after and before 
start vdoclip with fadein effect and end with fadeout effect
export the final vdo as before after.mp4 at 24fps"""
from moviepy.editor import * # pyright: ignore[reportMissingImports]
o=VideoFileClip("vdo img processing/vd3.mp4").subclip(0,10) # type: ignore
o1=VideoFileClip("vdo img processing/vd4.mp4").subclip(0,10)  # type: ignore
bw=o1.fx(vfx.blackwhite) # type: ignore

from moviepy.config import change_settings # pyright: ignore[reportMissingImports]
change_settings({
       "IMAGEMAGICK_BINARY":"C:\\Program Files\\ImageMagick-7.1.2-Q16-HDRI\\magick.exe"
})
txt1=TextClip("beforiieeee",fontsize=50,color="white") # type: ignore
txt=txt1.set_position((200,300)).set_duration(5)
comp1=CompositeVideoClip([o,txt]) # type: ignore

txt2=TextClip("afterieeee",fontsize=50,color="white") # type: ignore
txt=txt2.set_position((200,300)).set_duration(5)
comp2=CompositeVideoClip([bw,txt]) # type: ignore

arr=clips_array([[comp1,comp2]]) # type: ignore
fast=arr.fx(vfx.fadein,2).fx(vfx.fadeout,2) # type: ignore
arr.write_videofile("ba.mp4",fps=24)


"""Create a python prog using moviepy that takes vdoclip the prog shld create a yt shorts style vdo
apply fadein and fadeout effect to the vdoclip and export the final vdo as
short_vdo.mp4 at 30fps with resoulution 1080*1920"""
from moviepy.editor import * # type: ignore
o1=VideoFileClip("ba.mp4").subclip(0,10) # type: ignore
from PIL import Image # type: ignore
if not hasattr(Image, 'ANTIALIAS'):
    Image.ANTIALIAS = Image.Resampling.LANCZOS
resized=o1.resize((1080,1920))
resized.write_videofile("short_vdo.mp4",fps=30)


