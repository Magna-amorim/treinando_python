from tkinter import *
def click1():
    etiqueta['text'] = 'Beto'
def click2():
    etiqueta['text'] = 'Magna'
janela = Tk()
janela.title("Empresa")
#janela.iconbitmap('Icon.ico')
janela['bg']=('#808080')
janela.geometry('500x400+50+20')
etiqueta=Label(janela,text = "Olá Mundo", bg=('#808080'), cursor="dot")
etiqueta.pack()
botao=Button(janela, bg=('red'),text="Botao 1", padx='80', pady='20', command=click1)
botao.pack()
botao1=Button(janela, bg=('red'),text="Click", padx='80', pady='20', command=click2)
botao1.pack()
janela.mainloop()