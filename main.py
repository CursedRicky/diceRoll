import random as r
import customtkinter as ctk
from PIL import Image
import threading as t

comando: str = "4d6"


def roll():
    global comando
    comando = textbox.get("0.0", "end")
    tiro: int = 0
    a: str = ""
    b: str = ""
    ctrl: bool = False

    for let in comando:
        if not ctrl and let != "d":
            b += let
        elif let != "d":
            a += let
        else:
            ctrl = True

    for i in range(int(b)):
        t = r.randint(1, int(a))
        tiro += t

    totale.configure(text=f"Totale tiro: {tiro}")


root = ctk.CTk()
root.geometry("400x500")
root.title("Roll")
root.resizable(False, False)

titolo = ctk.CTkLabel(master=root, text="Tira dadi", font=("Calibri", 40))
titolo.pack(pady=5)

textbox = ctk.CTkTextbox(master=root, width=150, height=10, fg_color="#d2d2d2", text_color="#333333")
textbox.pack(pady=15)

tira = ctk.CTkButton(master=root, text="Tira", command=roll)
tira.pack(pady=5)

img = ctk.CTkImage(Image.open("d20.png"), size=(150, 150))
imgL = ctk.CTkLabel(master=root, image=img, text="")
imgL.pack(pady=10)

totale = ctk.CTkLabel(master=root, text="Totale tiro:", font=("Calibri", 25))
totale.pack(pady=5)

root.mainloop()
