import random as r
import customtkinter as ctk
from PIL import Image


def roll():
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
root.geometry("325x425")
root.title("Roll")
root.resizable(False, False)

frameDanni = ctk.CTkFrame(master=root)
frameDanni.pack(pady=20)

titolo = ctk.CTkLabel(master=frameDanni, text="Tira dadi danni", font=("Calibri", 40))
titolo.pack(pady=5, padx=20)

textbox = ctk.CTkTextbox(master=frameDanni, width=150, height=10, fg_color="#d2d2d2", text_color="#333333")
textbox.pack(pady=15)

tira = ctk.CTkButton(master=frameDanni, text="Tira", command=roll)
tira.pack(pady=5)

img = ctk.CTkImage(Image.open("d20.png"), size=(150, 150))
imgL = ctk.CTkLabel(master=frameDanni, image=img, text="")
imgL.pack(pady=10)

totale = ctk.CTkLabel(master=frameDanni, text="Totale tiro:", font=("Calibri", 25))
totale.pack(pady=10)

root.mainloop()
