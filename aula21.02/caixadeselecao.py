from tkinter import *
janela = Tk()
#fynção def
def funcao():
    if var1.get()== 1:
        etq1['text']='opção 1 selecionada'
    else:
        etq1['text']=''
    if var2.get()== 1:
        etq2['text']= 'opçaõ 2 selecionada'
    else:
        etq2['text']=''   
#titulo e icone
janela.title("Caixa de seleção")
janela.iconbitmap('icone.ico')
#declaração de checkBox
var1= IntVar()
Checkbutton(janela, text= 'opção 1', variable=var1).grid(row=0, padx=220)

var2 = IntVar()
Checkbutton(janela, text= 'opção 2', variable=var2).grid(row=1, padx=220)

#botão

botao=Button(janela, bg=('pink'),text="Selecionar", padx='10', pady='2.5', command=funcao)
botao.grid()

#etiqueta
etq1= Label(janela, text=' ')
etq1.grid()
etq2= Label(janela, text=' ')
etq2.grid()

#janela.geometry('500x300+50+200')
janela.mainloop()