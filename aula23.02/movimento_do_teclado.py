#movimentos do teclado
#canva 
from tkinter import*
janela=Tk()

def esquerda(event):
    x=-15
    y=0
    tela.move(circulo,x,y)

def direita(event):
    x=+15
    y=0
    tela.move(circulo,x,y)

def subir(event):
    x=0
    y=-15
    tela.move(circulo,x,y)

def descer(event):
    x=0
    y=+15
    tela.move(circulo,x,y)    

#dimensões do circulo
x=300
y=300

#criação do canva
tela=Canvas(janela, height=600, width=600, bg="white")
tela.pack()

#criação do circulo
circulo=tela.create_oval(x,y ,x+10, y+10, fill='blue')


#criação de eventos
janela.bind('<Left>', esquerda)
janela.bind('<Right>', direita)
janela.bind('<Up>', subir)
janela.bind('<Down>', descer)


janela.geometry('600x600+50+200')
janela.mainloop()