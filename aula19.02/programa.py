from tkinter import *
def click1():
    x=entrada1.get()
    y=entrada2.get()
    if x.isnumeric() and y.isnumeric():
        z= int(x)+int(y)
        etiqueta['text']=z
    else:
        etiqueta['text']='Entre com dados válidos'


janela = Tk()
janela.title("Empresa")
#janela.iconbitmap('icone.ico')
janela['bg']=('pink')
janela.geometry('500x400+50+200')
etiqueta1=Label(janela,text = "Primeiro Número", bg=('pink'))
etiqueta1.pack()
entrada1=Entry(janela, width=10,)
entrada1.pack()
etiqueta2=Label(janela,text = "Segundo Número", bg=('pink'))
etiqueta2.pack()
entrada2=Entry(janela, width=10,)
entrada2.pack()
etiqueta=Label(janela,text = " ", bg=('pink'))
etiqueta.pack()
botao=Button(janela, bg=('light blue'),text="Somar", padx='40', pady='10', command=click1)
botao.pack()
janela.mainloop()

