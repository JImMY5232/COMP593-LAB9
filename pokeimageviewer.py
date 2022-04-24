
from tkinter import *
from tkinter import ttk
import os
import sys
import ctypes
import requests
from pokeapi import get_poke_list, get_pokemon_img_url  
# create the main fuction
def main():
    #create a path 
    script_dir = sys.path[0]
    image_dir = os.path.join(script_dir, 'images')
    if not os.path.isdir(image_dir):
        os.makedirs(image_dir)
#crate root ttk
    root =Tk()
    root.title("pokemon Image Viewer")
    app_id = 'COMP.pokeimageviewer'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
    root.iconbitmap(os.path.join('pokeball_icon.ico'))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    

#create a frame for gui
    frm = ttk.Frame(root)
    frm.grid(sticky=(N,S,E,W))
    frm.columnconfigure(0, weight=1)
    frm.rowconfigure(0, weight=60)
    root.geometry('600x600')

    #create a image for default window
    img_pokemon = PhotoImage(file=os.path.join(script_dir,'pokeball.png'))
    Ibl_image = Label(frm,image=img_pokemon)
    Ibl_image.grid(row=0, column=0, padx=10, pady=10)
   
    #creating list of pokemon
    pokemon_list = get_poke_list(limit=1000)
    pokemon_list.sort()
    pokemon_sel_cbo = ttk.Combobox(frm, values=pokemon_list, state='readonly')
    pokemon_sel_cbo.set('Select a Pokemon')
    pokemon_sel_cbo.grid(row=1, column=0)
    #create new fuction for handle event
    def handle_pokemon_sel_cbo(event):
        """
        This is a fuction for handle all events in the gui

        :param param1: event
        :returns: none
        
        """
        pokemon_name = pokemon_sel_cbo.get()
        image_url = get_pokemon_img_url(pokemon_name)
        image_path =os.path.join(image_dir,pokemon_name +'.png')
        if down_image_frm_url(image_url, image_path):
            img_pokemon['file'] = image_path
            desktop_btn.state(['!disabled'])

    pokemon_sel_cbo.bind('<<ComboboxSelected>>', handle_pokemon_sel_cbo)
    #fuction for button
    def desktop_btn_click():
        
        """
        This is a fuction for create and make the button for set image as backgroud

        :param param1: 
        :returns: none
        
        """
        pokemon_name = pokemon_sel_cbo.get()
        image_path = os.path.join(image_dir, pokemon_name +'.png')
        set_desktop_bg(image_path)

    desktop_btn = ttk.Button(frm, text='Set as Desktop Image', command=desktop_btn_click)
    desktop_btn.state(['disabled'])
    desktop_btn.grid(row=2,column=0,padx=10,pady=10)

    root.mainloop()
# create a fuction which make the downloaded picture as system background

def set_desktop_bg(path):

    """
    This is a fuction for the path where image downloads

    :param param1: path
    :returns: none
    
    """

    try:
     ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
    except:
        print("Error setting desktop background image")

#created a fuction  for download the image from the url
def down_image_frm_url(url, path):

    """
        This is a fuction for download image from the url

        :param param1: url
        :param param2: path
        :returns: the path 
        
    """

    if os.path.isfile(path):
        return path

    resp_msg = requests.get(url)
    if resp_msg.status_code == 200:
        try:
            img_data =resp_msg.content
            with open(path, 'wb') as fp:
                fp.write(img_data)
            return path
        except:
            return
    else:
        print('Failed to get pokemon list.')
        print('Response code:',resp_msg.status_code)
        print(resp_msg.text) 
        
main()