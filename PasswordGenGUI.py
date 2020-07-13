import tkinter as tk
import random # Modulo random, che serve a generare caratteri random, usato per creare passwords
import string # Modulo stringa, usato per creare stringhe complesse coi caratteri random
from tkinter import messagebox
import pyperclip

nome_del_programma = ("PasswordGenerator")
version = '1'
pwd = 0

class Gui:
    def __init__(self,  master):
        master.title(nome_del_programma)
        master.geometry("500x100")

        self.master = master

        master.button1 = tk.Button(text="Genera", command=self.psswdgen)
        master.button1.pack(side=tk.BOTTOM)
        master.text1 = tk.Label(text="Scegli la lunghezza della password e clicca su genera")
        master.text1.pack()

        master.slider1 = tk.Scale(from_=8, to=100, length=200, resolution=1, orient=tk.HORIZONTAL)
        master.slider1.pack()

        self.menubar = Menubar(self)

    def psswdgen(self, chars=string.ascii_letters + string.digits + string.punctuation): # 1 - lettere maisc o min, 2 - cifre, 3 - simboli
        global pwd
        val1 = master.slider1.get()
        pwd = ''.join(random.choice(chars) for _ in range(val1)) # i caratteri per la password sono stati forniti come parametri
        pyperclip.copy(pwd)
        pyperclip.paste()
        box_title = nome_del_programma
        box_message = '''Password salvata nella clipboard'''
        messagebox.showinfo(box_title, box_message)

if __name__ == '__main__':
    master = tk.Tk()
    pt = Gui(master)
    master.mainloop()
