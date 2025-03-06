from io import BytesIO
from tkinter import *
from random import randint
from tkinter import messagebox
from captcha.image import ImageCaptcha
import os

# Verify that the font files exist
font_paths = [
    'fonts/ChelseaMarketsr.ttf',
    'fonts/DejaVuSanssr.ttf'
]

for font_path in font_paths:
    if not os.path.exists(font_path):
        raise FileNotFoundError(f"Font file not found: {font_path}")

image = ImageCaptcha(fonts=font_paths)

random = str(randint(100000, 999999))
data = image.generate(random)
assert isinstance(data, BytesIO)
image.write(random, 'out.png')

def verify():
    global random
    x = t1.get("0.0", END).strip()
    if x == random:
        messagebox.showinfo("Success", "Verified")
    else:
        messagebox.showinfo("Alert", "Not verified")
        refresh()

def refresh():
    global random
    random = str(randint(100000, 999999))
    data = image.generate(random)
    assert isinstance(data, BytesIO)
    image.write(random, 'out.png')
    photo = PhotoImage(file="out.png")
    l1.config(image=photo, height=100, width=200)
    l1.image = photo  # Keep a reference to avoid garbage collection
    UpdateLabel()

def UpdateLabel():
    photo = PhotoImage(file="out.png")
    l1.config(image=photo)
    l1.image = photo  # Keep a reference to avoid garbage collection

root = Tk()
photo = PhotoImage(file="out.png")

l1 = Label(root, image=photo, height=100, width=200)
t1 = Text(root, height=5, width=50)
b1 = Button(root, text="submit", command=verify)
b2 = Button(root, text="refresh", command=refresh)

l1.pack()
t1.pack()
b1.pack()
b2.pack()
root.mainloop()