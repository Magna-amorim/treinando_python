#canva 
from tkinter import*
janela=Tk()
janela.geometry('500x400+50+200')

#criação do canva
tela=Canvas(janela, height=500, width=500, bg="white")
tela.pack()

#criação de retangulo
retangulo=tela.create_rectangle(0, 0, 400, 300, fill="lightgreen")
 
#criação de poligono
poligono=tela.create_polygon(0,150, 200, 0, 400, 150, 200, 300, fill="lightyellow")

#criação de circulo
circulo=tela.create_oval(100, 50, 300, 250, fill="lightblue")

#criação de linha
linha=tela.create_line(100, 150, 300, 150, width=15, fill="white")

#texto
texto=tela.create_text(200, 150, fill="black", text="Ordem e Progresso")

janela.mainloop()