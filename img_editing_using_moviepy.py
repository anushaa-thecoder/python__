from moviepy.editor import ImageClip #type: ignore

# Load an image and create a video clip from it
clip = ImageClip("anmuu.jpg") 

# Set the duration of the clip (in seconds)
clip = clip.set_duration(5)

# Resize the image (optional)
from PIL import Image #type: ignore
if not hasattr(Image, 'ANTIALIAS'):
    Image.ANTIALIAS = Image.Resampling.LANCZOS
clip = clip.resize((640,400))  # Resize width to 640px, maintains aspect ratio

# Write the clip to a video file
clip.write_videofile("image_video.mp4",fps=24, codec="libx264")

