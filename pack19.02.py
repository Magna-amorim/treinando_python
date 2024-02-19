from tkinter import *

janela = Tk()
janela.geometry('500x500+100+100')

lb1=Label(janela, text= 'A' )
lb1.pack(side= LEFT)

lb2=Label(janela, text= 'B' )
lb2.pack(side= BOTTOM)

lb3=Label(janela, text= 'C')
lb3.pack(side= RIGHT)

lb3=Label(janela, text= 'D ')
lb3.pack(side= TOP)

janela.mainloop()