import os 
import random 
import PIL import image 
import tkinter as tk


def gatcha():
    path = 'C:\Users\ebisu\code\djangogirls\media\images'
    files = os.listdir
    index = random.randrange(0, len(files))
    image = Image.open(files[index])
    image.show()


pack_button = Button(window,text = "Pack",fg = "white",bg = "black", command = pack)
pack_button.grid(row = 2,colum = 1,padx = 10,pady = 5)

window.mainloop()

