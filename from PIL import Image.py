from PIL import Image
import os

pages = []

for i in range(1, 11):
    filename = f"static/comic_pages/page_{i}.png"

    if os.path.exists(filename):
        pages.append(Image.open(filename).convert("RGB"))

if len(pages) == 10:
    pages[0].save(
        "Lena_Sunny_Comic.pdf",
        save_all=True,
        append_images=pages[1:]
    )
    print("PDF created successfully!")
else:
    print("Please check the 10 comic pages.")

    