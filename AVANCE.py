#LIBRERIAS

from tkinter import *
from tkinter import ttk
import tkinter
from turtle import bgcolor
from matplotlib.pyplot import gray
from setuptools import Command
import sounddevice as sd
import numpy as np
import pygame
from PIL import ImageTk, Image

#APLICACION

class Aplicacion():
    def __init__(self):
        self.raiz = Tk()
        self.raiz.geometry('500x500')
        self.raiz.resizable(0,0)
        self.raiz.config(bg='lightgray')
        self.raiz.title('Prueba musical')
        self.raiz.iconbitmap('nota.ico')
        
        self.myframe=Frame()
        self.myframe.pack()
        self.myframe.config(bg='gray', width='300', height='300', cursor='cross', bd=20 ,relief='groove')
       
        self.music=Button(self.raiz, text='M', command=self.reproductor('do.wav'))
        self.music.place(x=0,y=0)
        self.music.config(bg='lightgray', fg='black')
       
        #IMAGEN
        
        image=Image.open('do.png')
        image=image.resize((350,130),Image.ADAPTIVE)  
        img=ImageTk.PhotoImage(image)
        lbl_img=Label(self.myframe, image=img)
        lbl_img.pack()
       
       
        #OPCIONES BOTONES

        self.laN=Button(self.raiz, text='LA', command=self.intenta_de_nuevo)
        self.laN.place(x=80,y=200)
        self.laN.config(bg='cyan', fg='black')

        self.solN=Button(self.raiz, text='SOL', command=self.intenta_de_nuevo)
        self.solN.place(x=180,y=200)
        self.solN.config(bg='cyan', fg='black')

        self.reN=Button(self.raiz, text='RE', command=self.intenta_de_nuevo)
        self.reN.place(x=280,y=200)
        self.reN.config(bg='cyan', fg='black')

        self.doN=Button(self.raiz, text='DO', command=self.buenardium)
        self.doN.place(x=380,y=200)
        self.doN.config(bg='cyan', fg='black')
        
        #BOTON DE SALIDA

        self.Salida=Button(self.raiz, text='Salir', command=self.raiz.destroy, cursor='pirate')
        self.Salida.place(x=220,y=450)
        self.Salida.config(bg='gold')
        
        self.raiz.mainloop()
    
    #FUNCIONES UTILIZADAS   

    def reproductor(self,cancion):
        pygame.mixer.init(frequency=44100)
        pygame.mixer.music.load(str(cancion))
        pygame.mixer.music.set_volume(1) 
        pygame.mixer.music.play(1) 

    def intenta_de_nuevo(self):
        txt=Label(self.raiz, text='Sigue intentando :c')
        txt.place(x=190,y=350)
        txt.config(bg='lightgray')

    def buenardium(self):
        txt=Label(self.raiz, text='¡¡¡ Felicitaciones :D !!!')
        txt.place(x=185,y=350)
        txt.config(bg='lightgray')

    def redimensionar(self,image,frame):  #En fase de pruebas (sale error)
        image=Image.open('do.png')
        image=image.resize((350,130),Image.ADAPTIVE)  
        img=ImageTk.PhotoImage(image)
        lbl_img=Label(frame, image=img)
        lbl_img.pack()
        
#COREER LA APLICACION

def main():
    mi_app = Aplicacion()
    return 0
   
if __name__ == '__main__':
    main()