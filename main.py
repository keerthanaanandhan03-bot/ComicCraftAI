from PIL import Image, ImageDraw, ImageFont
import os
import math

# -------------------------------------------------
# COMICCRAFTAI
# 10 PAGE LENA & SUNNY FRIENDSHIP COMIC
# -------------------------------------------------

os.makedirs("static/comic_pages", exist_ok=True)

W = 1000
H = 1300

# ---------- FONTS ----------
try:
    title_font = ImageFont.truetype("arialbd.ttf", 42)
    name_font = ImageFont.truetype("arialbd.ttf", 25)
    dialogue_font = ImageFont.truetype("arial.ttf", 24)
    small_font = ImageFont.truetype("arial.ttf", 20)
except:
    title_font = ImageFont.load_default()
    name_font = ImageFont.load_default()
    dialogue_font = ImageFont.load_default()
    small_font = ImageFont.load_default()


# ---------- DRAW CHARACTER ----------
def draw_character(draw, x, y, hair, shirt, expression="happy", name=""):
    # Hair
    draw.ellipse(
        (x - 45, y - 120, x + 45, y - 30),
        fill=hair,
        outline="black",
        width=4
    )

    # Face
    draw.ellipse(
        (x - 40, y - 105, x + 40, y - 25),
        fill="#FFD6B0",
        outline="black",
        width=3
    )

    # Eyes
    if expression == "sad":
        draw.arc((x - 25, y - 75, x - 5, y - 55), 200, 340,
                 fill="black", width=3)
        draw.arc((x + 5, y - 75, x + 25, y - 55), 200, 340,
                 fill="black", width=3)
    else:
        draw.ellipse((x - 25, y - 75, x - 12, y - 60), fill="black")
        draw.ellipse((x + 12, y - 75, x + 25, y - 60), fill="black")

    # Smile / mouth
    if expression == "sad":
        draw.arc((x - 18, y - 55, x + 18, y - 35), 200, 340,
                 fill="black", width=3)
    else:
        draw.arc((x - 20, y - 55, x + 20, y - 25), 20, 160,
                 fill="black", width=3)

    # Body
    draw.rounded_rectangle(
        (x - 60, y - 20, x + 60, y + 150),
        radius=25,
        fill=shirt,
        outline="black",
        width=4
    )

    # Arms
    draw.line(
        (x - 55, y + 10, x - 110, y + 70),
        fill="black",
        width=7
    )

    draw.line(
        (x + 55, y + 10, x + 110, y + 70),
        fill="black",
        width=7
    )

    # Legs
    draw.line(
        (x - 25, y + 145, x - 45, y + 230),
        fill="black",
        width=7
    )

    draw.line(
        (x + 25, y + 145, x + 45, y + 230),
        fill="black",
        width=7
    )

    # Name
    draw.text(
        (x - 40, y + 245),
        name,
        fill="black",
        font=name_font
    )


# ---------- SPEECH BUBBLE ----------
def speech(draw, x, y, w, h, text, tail="left"):
    draw.rounded_rectangle(
        (x, y, x + w, y + h),
        radius=25,
        fill="white",
        outline="black",
        width=4
    )

    if tail == "left":
        draw.polygon(
            [(x + 35, y + h),
             (x + 15, y + h + 35),
             (x + 70, y + h - 5)],
            fill="white",
            outline="black"
        )
    else:
        draw.polygon(
            [(x + w - 70, y + h),
             (x + w - 20, y + h + 35),
             (x + w - 30, y + h - 5)],
            fill="white",
            outline="black"
        )

    draw.text(
        (x + 20, y + 18),
        text,
        fill="black",
        font=dialogue_font
    )


# ---------- DECORATIONS ----------
def stars(draw):
    for x, y in [(100, 180), (850, 180), (150, 1050), (850, 1080)]:
        draw.text((x, y), "★", fill="#FFD700", font=title_font)


def hearts(draw):
    for x, y in [(100, 300), (850, 320), (470, 1100)]:
        draw.text((x, y), "♥", fill="#FF4F81", font=title_font)


# ---------- PAGE CREATOR ----------
def create_page(number, title, bg, dialogue1, dialogue2, scene):

    page = Image.new("RGB", (W, H), bg)
    draw = ImageDraw.Draw(page)

    # Header
    draw.rounded_rectangle(
        (40, 30, 960, 120),
        radius=30,
        fill="#FFFFFF",
        outline="#222222",
        width=5
    )

    draw.text(
        (300, 55),
        f"LENA & SUNNY",
        fill="#6A1B9A",
        font=title_font
    )

    # Page number
    draw.text(
        (820, 65),
        f"{number}/10",
        fill="#333333",
        font=small_font
    )

    # Main comic panel
    draw.rounded_rectangle(
        (50, 150, 950, 1080),
        radius=35,
        fill=bg,
        outline="#222222",
        width=7
    )

    # Scene
    if scene == "school":
        draw.rectangle((120, 650, 880, 1000), fill="#7BC96F")

        draw.rectangle(
            (350, 400, 650, 650),
            fill="#FFF3B0",
            outline="black",
            width=5
        )

        draw.polygon(
            [(320, 400), (500, 270), (680, 400)],
            fill="#FF6B6B",
            outline="black"
        )

        draw.text((425, 470), "SCHOOL", fill="#333333", font=name_font)

    elif scene == "library":
        draw.rectangle((100, 300, 900, 900), fill="#D7B899")

        for y in [400, 550, 700]:
            draw.rectangle(
                (150, y, 850, y + 25),
                fill="#5D4037"
            )

        for x in range(170, 830, 80):
            draw.rectangle(
                (x, 330, x + 50, 390),
                fill="#FF6F61"
            )

    elif scene == "park":
        draw.rectangle((100, 700, 900, 1000), fill="#79D279")

        # Tree
        draw.rectangle((700, 450, 750, 750), fill="#8D5524")
        draw.ellipse((620, 330, 830, 520), fill="#55B947")

        # Sun
        draw.ellipse((120, 220, 220, 320), fill="#FFD54F")

    elif scene == "classroom":
        draw.rectangle((100, 650, 900, 1000), fill="#DDEEFF")

        draw.rectangle(
            (150, 250, 850, 450),
            fill="#90CAF9",
            outline="black",
            width=4
        )

        draw.text(
            (400, 330),
            "FRIENDS",
            fill="#1A237E",
            font=name_font
        )

    else:
        draw.rectangle((100, 700, 900, 1000), fill="#B2EBF2")

    # Characters
    draw_character(
        draw,
        330,
        720,
        "#4A2C20",
        "#FF7EB3",
        "happy",
        "Lena"
    )

    draw_character(
        draw,
        670,
        720,
        "#2B1B17",
        "#64B5F6",
        "happy",
        "Sunny"
    )

    # Speech bubbles
    speech(
        draw,
        100,
        210,
        360,
        100,
        dialogue1,
        "left"
    )

    speech(
        draw,
        540,
        330,
        360,
        100,
        dialogue2,
        "right"
    )

    stars(draw)
    hearts(draw)

    # Footer
    draw.text(
        (350, 1150),
        "A STORY ABOUT TRUE FRIENDSHIP",
        fill="#6A1B9A",
        font=small_font
    )

    # Save
    filename = f"static/comic_pages/page_{number}.png"
    page.save(filename)


# -------------------------------------------------
# 10 PAGES
# -------------------------------------------------

stories = [
    ("A NEW DAY", "#B3E5FC",
     "Hi Sunny! Ready for school?",
     "Yes! Let's go together!",
     "school"),

    ("A MYSTERIOUS NOTE", "#FFF9C4",
     "Sunny, look! What's this note?",
     "I think it is a clue!",
     "school"),

    ("THE MYSTERY", "#D1C4E9",
     "Should we solve the mystery?",
     "Of course! Together!",
     "school"),

    ("THE LIBRARY", "#FFE0B2",
     "Maybe the next clue is here.",
     "Let's search the library!",
     "library"),

    ("A NEW CLUE", "#C8E6C9",
     "Lena! I found something!",
     "Wow! We are getting closer!",
     "library"),

    ("THE OLD CLASSROOM", "#FFCCBC",
     "This classroom looks strange.",
     "Let's see what's inside.",
     "classroom"),

    ("THE SECRET BOX", "#B2DFDB",
     "Look! There is a box!",
     "What could be inside?",
     "classroom"),

    ("THE SURPRISE", "#F8BBD0",
     "Wow! We found the secret!",
     "We solved it together!",
     "park"),

    ("BEST TEAM", "#D1C4E9",
     "We make a great team!",
     "Yes! Best friends forever!",
     "park"),

    ("TRUE FRIENDSHIP", "#B3E5FC",
     "I'm glad we did this together.",
     "That's what best friends do!",
     "park")
]


# Create all pages
for number, data in enumerate(stories, start=1):
    create_page(number, *data)


print("===================================")
print("10 PAGE COMIC CREATED SUCCESSFULLY!")
print("Characters: Lena and Sunny")
print("===================================")
print("Open: static/comic_pages")

from PIL import Image
import os

pages = []

for i in range(1, 11):
    filename = f"static/comic_pages/page_{i}.png"

    if os.path.exists(filename):
        image = Image.open(filename).convert("RGB")
        pages.append(image)

if pages:
    pdf_file = "Lena_Sunny_Comic.pdf"

    pages[0].save(
        pdf_file,
        save_all=True,
        append_images=pages[1:]
    )

    print("PDF created successfully!")
    print("File:", pdf_file)
else:
    print("Comic pages not found!")