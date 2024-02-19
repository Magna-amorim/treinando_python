from tkinter import *

janela = Tk()
janela.geometry('400x200+100+100')

lb1=Label(janela, text = 'Login: ')
lb1.grid(column=0, row=0)

En1 = Entry(janela)
En1.grid(column=1, row=0, padx= (50, 50), pady=(20,20))

lb2=Label(janela, text = 'Senha: ')
lb2.grid(column=0, row=1)

En2 = Entry(janela)
En2.grid(column=1, row=1)

btn1=Button(janela, text='Avançar')
btn1.grid(columnspan=2, row=2, pady=(20,20) )




janela.mainloop()