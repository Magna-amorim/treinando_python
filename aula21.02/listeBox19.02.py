'''
listebox e scrollbar
'''

from tkinter import *
janela = Tk()
def selecao():
    etq['text']='local é ' + lista.get(ANCHOR)


etq2=Label(janela, text=' Qual estado voce mora?')
etq2.pack()

frame= Frame(janela)
Scrollbar = Scrollbar(frame, orient= VERTICAL)
lista= Listbox(frame, width=20, height=5, yscrollcommand=Scrollbar.set)
Scrollbar.config(command= lista.yview)
Scrollbar.pack(side= RIGHT, fill= Y)
frame.pack()
lista.pack()
minhalista=['São Paulo', 'Rio de janeiro', 'Minas Gerais', 'Paraná', 'Mato Grosso', 'Amazonas', 'Ceara', 'Santa Catarina']

for item in minhalista:
    lista.insert(END, item)

btn=Button(janela, text='Selecionado', command=selecao )
btn.pack()
etq=Label(janela, text='')
etq.pack()
janela.geometry('500x400+50+200')
janela.mainloop()
