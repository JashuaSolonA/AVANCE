from cProfile import label
from tkinter import *
from tkinter import ttk
import tkinter
from matplotlib.pyplot import gray
import sounddevice as sd
import numpy as np


class Aplicacion():
    def __init__(self):
        self.raiz = Tk()
        self.raiz.geometry('500x500')
        self.raiz.resizable(1,1)
        self.raiz.config(bg='lightgray', cursor='pirate')
        self.raiz.title('Prueba musical')
        self.raiz.iconbitmap('nota.ico')
        
        self.Salida=Button(self.raiz, text='Salir', command=self.raiz.destroy)
        self.Salida.place(x=220,y=450)
        self.Salida.config(bg='gold')
        
        self.myframe=Frame()
        self.myframe.pack()
        self.myframe.config(bg='gray', width='300', height='300', cursor='hand1', bd=20 ,relief='groove')
       
        self.notita=Button(self.raiz, text='LA', command=self.reproducir(10,4))
        self.notita.place(x=110,y=200)
        self.notita.config(bg='cyan', fg='white')
        
        self.la=tkinter.PhotoImage(file='LA.png')
        self.label_la=tkinter.Label(self.myframe, image=self.la)
        self.label_la.pack()
        
        self.raiz.mainloop()
    
    def frecuencia_mk(self,nota,octava):
        exponente=(octava-4)*12+(nota-10)
        return 440 * ((2**(1/12))**exponente)
        
    def reproducir(self,nota,octava,time=1000,framerate=44100):
        frecuencia= self.frecuencia_mk(nota,octava)
        t = np.linspace(0,time/1000,int(framerate*time/1000))
        ondita = np.sin(2* np.pi * frecuencia * t)
        sd.play(ondita,framerate)
        sd.wait()
    
def main():
    mi_app = Aplicacion()
    return 0
    
if __name__ == '__main__':
    main()
