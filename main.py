import random as r
import customtkinter as ctk
from PIL import Image


def roll() -> None:
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


def rollSV() -> None:
    dado1.configure(text=f"Dado 1: {r.randint(1, 20)}")
    dado2.configure(text=f"Dado 2: {r.randint(1, 20)}")


root = ctk.CTk()
root.geometry("610x400")
root.title("Roll")
root.resizable(False, False)

frameDanni = ctk.CTkFrame(master=root)
frameDanni.grid(pady=10, padx=10, column=0, row=0)

frameSV = ctk.CTkFrame(master=root)
frameSV.grid(pady=10, padx=10, column=1, row=0)

# Tiro danni

titoloDanni = ctk.CTkLabel(master=frameDanni, text="Tira dadi danni", font=("Calibri", 40))
titoloDanni.pack(pady=5, padx=20)

textbox = ctk.CTkTextbox(master=frameDanni, width=150, height=10, fg_color="#d2d2d2", text_color="#333333")
textbox.pack(pady=15)

tira = ctk.CTkButton(master=frameDanni, text="Tira", command=roll)
tira.pack(pady=5)

img = ctk.CTkImage(Image.open("d20.png"), size=(150, 150))
imgL = ctk.CTkLabel(master=frameDanni, image=img, text="")
imgL.pack(pady=10)

totale = ctk.CTkLabel(master=frameDanni, text="Totale tiro:", font=("Calibri", 25))
totale.pack(pady=10)

# Vantaggio Svantaggio

titoloSV = ctk.CTkLabel(master=frameSV, text="Tira con SvaVan", font=("Calibri", 40))
titoloSV.pack(pady=5, padx=20)

tira = ctk.CTkButton(master=frameSV, text="Tira", command=rollSV)
tira.pack(pady=5)

img = ctk.CTkImage(Image.open("d20.png"), size=(150, 150))
imgL = ctk.CTkLabel(master=frameSV, image=img, text="")
imgL.pack(pady=10)

dado1 = ctk.CTkLabel(text="Dado 1", master=frameSV, font=("Calibri", 20))
dado1.pack(pady=13)

dado2 = ctk.CTkLabel(text="Dado 2", master=frameSV, font=("Calibri", 20))
dado2.pack(pady=13)

root.mainloop()
