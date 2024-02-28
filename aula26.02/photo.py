from tkinter import*
janela=Tk()

#imagem dentro de uma pasta
img=PhotoImage(file="aula26.02\imagem\img.png")
etq=Label(janela,image=img)
etq.pack()

janela.mainloop()