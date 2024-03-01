from tkinter import*
jn=Tk()
x= Scale(jn, from_=00,to = 100)
x.pack()

#criação de função def
def avaliacao():
    Etq= Label(jn, text=f'A avaliação foi {x.get()}').pack()

#botão
bt=Button(jn, text= "avaliar", command=avaliacao)
bt.pack()



jn.geometry('500x400+50+200')
mainloop()