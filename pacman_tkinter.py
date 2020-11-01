"""Pacman"""

import tkinter as tk
import os

class Ghost(tk.Canvas):
    def __init__(self, name, direction):
        tk.Canvas.__init__(self, app)
        self.name = name
        self.direction = direction

        if self.name == 'Clyde':
            if self.direction == 'right':
                self.config(width=40, height=49, bg="white")
                img = tk.PhotoImage(file='Clyde_right.gif')
                img_2 = img.subsample(12, 12)
                self.create_image(22, 26, image=img_2)


def map_ext():
    traits = []
    traits.append(tk.Canvas(app,width=520, height=10,bd=0, bg='black'))
    traits[0].create_rectangle(0,4,520,7, fill='blue', outline='blue')
    traits[0].place(x=290,y=100) #long allongé haut

    traits.append(tk.Canvas(app,width=230, height=10,bd=0, bg='black'))
    traits[1].create_rectangle(0,4,230,7, fill='blue', outline='blue')
    traits[1].place(x=300,y=110)  #court allongé haut

    traits.append(tk.Canvas(app,width=230, height=10,bd=0, bg='black'))
    traits[2].create_rectangle(0,4,230,7, fill='blue', outline='blue')
    traits[2].place(x=570,y=110)  #court allongé haut 2

    traits.append(tk.Canvas(app,width=10, height=80,bd=0, bg='black'))
    traits[3].create_rectangle(2,4,5,80, fill='blue', outline='blue')
    traits[3].place(x=530,y=110)  #court vertical haut

    traits.append(tk.Canvas(app,width=5, height=80,bd=0, bg='black'))
    traits[4].create_rectangle(2,4,5,80, fill='blue', outline='blue')
    traits[4].place(x=570,y=110)  #court vertical haut 2

    traits.append(tk.Canvas(app,width=40, height=10,bd=0, bg='black'))
    traits[5].create_rectangle(2,4,40,7, fill='blue', outline='blue')
    traits[5].place(x=530,y=180)  #court horizontal haut fermer obstacle milieu

    traits.append(tk.Canvas(app,width=5, height=200,bd=0, bg='black'))
    traits[6].create_rectangle(0,0,5,200, fill='blue', outline='blue')
    traits[6].place(x=290,y=106)  #long vertical haut gauche

    traits.append(tk.Canvas(app,width=5, height=180,bd=0, bg='black'))
    traits[7].create_rectangle(0,0,5,180, fill='blue', outline='blue')
    traits[7].place(x=300,y=116)  #long vertical haut gauche 2

    traits.append(tk.Canvas(app,width=100, height=5,bd=0, bg='black'))
    traits[8].create_rectangle(2,0,100,5, fill='blue', outline='blue')
    traits[8].place(x=290,y=305)  #court allongé haut

    traits.append(tk.Canvas(app,width=100, height=5,bd=0, bg='black'))
    traits[9].create_rectangle(2,0,100,5, fill='blue', outline='blue')
    traits[9].place(x=300,y=295)  #court allongé haut

    

def create_app():
    global app
    app = tk.Tk()
    app.title("Pacman")
    app.minsize(1270, 800)
    app.resizable(width=True, height=True)
    app.geometry("50x100+0+0")
    app.configure(bg="black")

def main():

    global app, Frame, clyde_right

    create_app()
    Frame = tk.Frame(app, bg='navy')
    Frame2 = tk.Frame(app, bg='navy')

    os.chdir("C:/Users/cleme/Desktop/Documents/1. DOCUMENTS CLEMENT/TRAVAIL/Post BAC/projets personnels info/MINI JEUX/Pacman")

    can = tk.Canvas(app,width=29, height=36, bd=0, bg='black')
    can.place(x=200,y=150)
    img = tk.PhotoImage(file='Clyde_right.gif')
    img_2 = img.subsample(16, 16)
    can.create_image(17,19,image=img_2)

    map_ext()

    app.mainloop()

if __name__=='__main__':
    main()
