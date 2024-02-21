# barra de progressao

from tkinter import *
from tkinter.ttk import*

janela = Tk()
janela.geometry('600x300')

def funcao():
    barra['value']= barra['value']+10
    etq['text']=barra['value']

barra= Progressbar(janela, length=500)
barra['value']=0
barra.pack()

btn= Button(janela, text='Avançar', command= funcao)
btn.pack()

etq= Label(janela, text= '0')
etq.pack()
janela.mainloop()


