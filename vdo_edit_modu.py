from moviepy.editor import * # pyright: ignore[reportMissingImports]
o=VideoFileClip(r"C:\Users\DEll\OneDrive\Desktop\python adv\vdo img processing\vd1.mp4") # type: ignore
# o.preview()

# s=o.subclip(0,5)
# # s.preview()

# s.write_videofile("out.mp4")
# # giff=s.write_gif("giffy.gif")
# # giff.preview()

# rotated=o.rotate(180)
# # rotated.preview()

# # from PIL import Image # type: ignore
# # if not hasattr(Image, 'ANTIALIAS'):
# #     Image.ANTIALIAS = Image.Resampling.LANCZOS
# # resized=o.resize(width=200)
# # resized.preview()

# cut=o.cutout(0,8)
# # cut.preview()

# marg=o.margin(20,color=(255,255,0))
# # marg.preview()

# fast=o.fx(vfx.speedx,0.5) # type: ignore
# # fast.preview()

# noiseless=o.without_audio()
# # noiseless.preview()

# duration=o.set_duration(8)
# # duration.preview()

# # #layout:
# # a=VideoFileClip(r"C:\Users\DEll\OneDrive\Desktop\python adv\vdo img processing\vd2.mp4").subclip(0,5) # type: ignore
# # b=VideoFileClip(r"C:\Users\DEll\OneDrive\Desktop\python adv\vdo img processing\vd4.mp4").subclip(0,5) # type: ignore
# # d=VideoFileClip(r"C:\Users\DEll\OneDrive\Desktop\python adv\vdo img processing\vd3.mp4").subclip(0,5)# type: ignore
# # arr=clips_array([[a,o],[b,d]]) # type: ignore
# # # arr.preview()
# # sav=arr.write_videofile("anu.mp4")

# #fadein and fadeout:
# fast=o.fx(vfx.fadein,4).fx(vfx.fadeout,4) # type: ignore
# # fast.preview()

# #black and white:
# bw=o.fx(vfx.blackwhite) # type: ignore
# bw.preview()

#loop:
# loo=o.fx(vfx.loop,n=2) # type: ignore
# # loo.preview()
# savv=loo.write_videofile("looie.mp4")

#concatenate two videos:
# v=concatenate_videoclips([b,d])  # type: ignore
# v.write_videofile("conc.mp4")


#adding text on video:
from moviepy.config import change_settings # pyright: ignore[reportMissingImports]
change_settings({
       "IMAGEMAGICK_BINARY":"C:\\Program Files\\ImageMagick-7.1.2-Q16-HDRI\\magick.exe"
})
# txt=TextClip("Helloiieeee",fontsize=50,color="white") # type: ignore
# txt=txt.set_position((200,300)).set_duration(5)
# comp=CompositeVideoClip([o,txt]) # type: ignore
# a=comp.write_videofile("anuma.mp4")


#save scrrenshot:
# a=VideoFileClip(r"C:\Users\DEll\OneDrive\Desktop\python adv\vdo img processing\vd2.mp4") #type: ignore
# a.save_frame("test.jpg")
# a.save_frame("anmuu.jpg",t=3)
 
o.audio.write_audiofile("extract.mp3")
pq=o.without_audio()
ne=pq.write_videofile("xyz.mp4")
q=VideoFileClip("xyz.mp4") #type: ignore
audio=AudioFileClip("extract.mp3")#type: ignore
clip_with_audio=q.set_audio(audio)
clip_with_audio.write_videofile("withsong.mp4")