#radiobutton para somente uma seleção

from tkinter import *
janela = Tk()
#fynção def

def sel():
   selecionado = 'Voce selecionou a opção ' + str(var.get())
   etq1['text'] = selecionado
    
#titulo e icone
janela.title("Caixa de seleção")
janela.iconbitmap('icone.ico')

#declaração de radiobutton
var= IntVar()
rb1= Radiobutton(janela, text= 'opção 1', variable=var, value=1)
rb1.pack()


rb2= Radiobutton(janela, text= 'opção 2', variable=var, value=2)
rb2.pack()


rb3= Radiobutton(janela, text= 'opção 3', variable=var, value=3)
rb3.pack()

#botão

botao=Button(janela, bg=('pink'),text="Selecionar", padx='10', pady='2.5',command=sel)
botao.pack()

#etiqueta
etq1= Label(janela, text=' ')
etq1.pack()


janela.geometry('500x300+50+200')
janela.mainloop()