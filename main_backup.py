from PIL import Image, ImageDraw, ImageFont
import os

# Comic settings
WIDTH = 1000
HEIGHT = 800

# Create white comic page
comic = Image.new("RGB", (WIDTH, HEIGHT), "white")
draw = ImageDraw.Draw(comic)

# Try to use a nice font
try:
    title_font = ImageFont.truetype("arial.ttf", 32)
    text_font = ImageFont.truetype("arial.ttf", 22)
except:
    title_font = ImageFont.load_default()
    text_font = ImageFont.load_default()

# Title
draw.text((350, 20), "COMICCRAFTAI", fill="black", font=title_font)

# Four panels
panels = [
    (40, 80, 480, 350),
    (520, 80, 960, 350),
    (40, 400, 480, 670),
    (520, 400, 960, 670)
]

for panel in panels:
    draw.rectangle(panel, outline="black", width=4)

# Comic story
story = [
    ("Panel 1", "A student finds a magical pencil."),
    ("Panel 2", "Everything drawn with it becomes real!"),
    ("Panel 3", "The student uses it to help friends."),
    ("Panel 4", "The magical adventure begins!")
]

# Add text to panels
for panel, (heading, text) in zip(panels, story):
    x1, y1, x2, y2 = panel

    draw.text(
        (x1 + 20, y1 + 20),
        heading,
        fill="black",
        font=title_font
    )

    draw.text(
        (x1 + 20, y1 + 80),
        text,
        fill="black",
        font=text_font
    )

# Create output folder
os.makedirs("static/exports", exist_ok=True)

# Save comic
output_file = "static/exports/my_comic.png"
comic.save(output_file)

print("Comic created successfully!")
print("Saved to:", output_file)
