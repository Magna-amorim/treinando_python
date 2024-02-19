#frame

from tkinter import *
janela = Tk()
janela.geometry('500x400+50+200')

frame1 = LabelFrame(janela, padx=20, pady=20, bg= "lightblue")
frame1.grid(column=0, row=0)


etiqueta=Label(frame1, text= "Etiqueta 1")
etiqueta.pack()

bt1=Button(frame1, text='Botão 1')
bt1.pack()


frame2 = LabelFrame(janela, padx=20, pady=20, bg= "pink")
frame2.grid(column=1, row=0)


etiqueta=Label(frame2, text= "Etiqueta 2")
etiqueta.pack()

bt2=Button(frame2, text='Botão 2')
bt2.pack()



janela.mainloop()