# Toplevel, menu de janela
from tkinter import*

def abrir():print, "Abrir"
def salvar():print, "Salvar"
def ajuda():print, "Ajuda"
top=Tk()

principal=Menu(top)
arquivo=Menu(principal)
arquivo.add_command(label="Abrir", command=abrir)
arquivo.add_command(label="Salvar", command=salvar)
principal.add_cascade(label="Arquivo", menu=arquivo)
principal.add_command(label="Ajuda", command=ajuda)
top.configure(menu=principal)


top.mainloop()