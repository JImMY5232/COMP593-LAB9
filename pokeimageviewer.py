from cProfile import label
from tkinter import *
from tkinter import ttk
import os
import sys
import ctypes
import types
from pokeapi import get_pokemon_info


def main():
    script_dir = sys.path[0]

    root =Tk()
    root.title("pokemon Image Viewer")
    app_id = 'COMP593.PokemonImageViewer'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
    root.iconbitmap(os.path.join('pokeball_icon.ico'))

    frm = ttk.Frame(root)
    frm.grid()
    
    img_pokemon = PhotoImage(file=os.path.join(script_dir,'pokeball.png'))
    Ibl_image = Label(frm,image=img_pokemon)
    Ibl_image.grid(row=0, column=0)
    


    root.mainloop()



main()