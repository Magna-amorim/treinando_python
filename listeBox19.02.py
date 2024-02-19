from tkinter import *
janela = Tk()
def selecao():
    etq['text']=lista.get(ANCHOR)

lista= Listbox(janela)
lista.pack()
minhalista=['São Paulo', 'Rio de janeiro', 'Minas Gerais']

for item in minhalista:
    lista.insert(END, item)

btn=Button(janela, text='Selecionado', command=selecao )
btn.pack()

etq=Label(janela, text=' ')
etq.pack()


janela.geometry('500x400+50+200')
janela.mainloop()