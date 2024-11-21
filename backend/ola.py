from moviepy.editor import TextClip

# Ensure the font path is correct
font_path = "C:\\Windows\\Fonts\\Arial.ttf"  # or the full path to the font file

# Create the TextClip with the correct arguments
txt_clip = TextClip("ola mundo", font=font_path, color='white', size=(400, 100), align="center")

# Preview the text clip
txt_clip.preview()
