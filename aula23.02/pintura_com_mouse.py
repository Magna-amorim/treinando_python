#pintura no Canvas com mouse 
from tkinter import*
janela=Tk()

def pintar(event):
    x1,y1= (event.x-3), (event. y-3)
    x2,y2= (event.x+3), (event. y+3)
    tela.create_oval(x1,y1,x2,y2, fill='black')

#definicao do botao limpar
def limpar():
    tela.delete('all') 
tela =Canvas(janela, height= 600, width=1200, bg="white")
tela.pack()


#criação de evento
tela.bind('<B1-Motion>', pintar)
# o b1 motion define o botao esquerdo do mouse
btn=Button(janela, text="limpar", command=limpar)
btn.pack()
janela.mainloop()