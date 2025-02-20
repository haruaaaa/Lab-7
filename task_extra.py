import tkinter as tk
import requests
from io import BytesIO
from PIL import Image, ImageTk
import random

def get_fox():
    num = random.randint(1, 123)
    url = f"https://randomfox.ca/images/{num}.jpg"
    return url


def new_fox():
    take = requests.get(get_fox())
    image_data = Image.open(BytesIO(take.content))
    img = ImageTk.PhotoImage(image_data)
    label.config(image=img)
    label.image = img


window = tk.Tk()
window.title("Генератор лисиц")

label = tk.Label(window)
label.pack()


button = tk.Button(window, text="Сгенерировать лису", command=new_fox)
button.place(relx=0.5, rely=0.1, anchor="center")

new_fox()
window.mainloop()