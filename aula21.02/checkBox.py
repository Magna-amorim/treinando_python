#checkBox ou caixa de seleçao, pode ser para fazer varias opções 

from tkinter import *
master = Tk()

var1= IntVar()
Checkbutton(master, text= 'male', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text= 'female', variable=var2).grid(row=1, sticky=W)

etq1= Label(janela, text='')
etq1.pack()
etq2= Label(janela, text='')
etq2.pack
botao=Button(janela, bg=('pink'),text="Selecionar", padx='10', pady='2.5')
botao.grid()





master.geometry('200x300+50+200')
mainloop()