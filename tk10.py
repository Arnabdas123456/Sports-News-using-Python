from tkinter import *
from PIL import ImageTk, Image


def every_100(text):
    final_text = ""
    for i in range(0, len(text)):
        final_text = final_text+text[i]
        if i % 100 == 0 and i != 0:
            final_text = final_text+"\n"
    return final_text


root = Tk()
root.geometry("1000x1000")
root.title("our news")

texts = []
photos = []

for i in range(0, 3):
    with open(f"{i+1}.txt", encoding="utf-8") as f:
        text = f.read()
        texts.append(every_100(text))
    image = Image.open(f"{i+1}.png")
    image = image.resize((200, 150))
    photos.append(ImageTk.PhotoImage(image))

f = Frame(root, width=800, height=70)
Label(f, text="Sports News", font="lucida 33 bold").pack()
Label(f, text="April 9, 2024", font="lucida 20 bold").pack()
f.pack()

f1 = Frame(root, width=900, height=200, pady=20)
Label(f1, text="Virat Kholi", font="lucida 15 bold").pack()
Label(f1, text=texts[0], padx=22, pady=22,
      font="comicsansns 10").pack(side="left")
Label(f1, image=photos[0], anchor="e").pack()
f1.pack(anchor="w")

f2 = Frame(root, width=900, height=200, pady=30, padx=22)
Label(f2, text="CR7", font="lucida 15 bold").pack()
Label(f2, text=texts[1], padx=22, pady=22,
      font="comicsansns 10").pack(side="right")
Label(f2, image=photos[1], anchor="e", padx=22).pack()
f2.pack(anchor="w")

f3 = Frame(root, width=900, height=200, pady=34)
Label(f3, text="Ms Dhoni", font="lucida 15 bold", pady=8).pack()
Label(f3, text=texts[2], padx=22, pady=22,
      font="comicsansns 10").pack(side="left")
Label(f3, image=photos[2], anchor="e", padx=20).pack()
f3.pack(anchor="w")


root.mainloop()
