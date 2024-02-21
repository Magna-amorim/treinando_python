from tkinter import *
janela = Tk()

etq1=Label(janela, text=' Qual o seu nome?')
etq1.pack()

entrada1=Entry(janela, width=50,)
entrada1.pack()

etq2=Label(janela, text=' Qual o sexo?', pady=15)
etq2.pack()

var= IntVar()
rb1= Radiobutton(janela, text= 'Masculino', variable=var, value=1)
rb1.pack()


rb2= Radiobutton(janela, text= 'Feminino', variable=var, value=2)
rb2.pack()

etq3=Label(janela, text=' Qual a unidade do seu curso?', pady=15)
etq3.pack()

janela.geometry('500x300+50+200')
janela.mainloop()