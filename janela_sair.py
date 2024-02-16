from tkinter import *
janela = Tk()
etiqueta=Label(janela, font=20, text = "Olá Magna")
janela.geometry('500x400+50+200')
etiqueta.pack()
botao=Button(janela, bg=('light blue'),text="Fechar", padx='20', pady='12',command= janela.quit)
botao.pack()
janela.mainloop()

