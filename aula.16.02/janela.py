from tkinter import *
def click1():
    etiqueta['text'] = 'botao1'
janela = Tk()
janela.title("Empresa")
#janela.iconbitmap('Icon.ico')
janela['bg']=('#808080')
janela.geometry('500x400+50+20')
etiqueta=Label(janela,text = "Olá Magna", bg=('#808080'), cursor="dot")
etiqueta.pack()
botao=Button(janela, bg=('red'),text="Botao 1", padx='80', pady='20', command=click1)
botao.pack()

janela.mainloop()