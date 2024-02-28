# Toplevel, menu de janela
from tkinter import*
jn=Tk()
#def comando editar
def edit1():
    texto1['text']= 'Editado'
def edit2():
    texto2['text']= 'Editado'
#comando excluir
def del1():
    texto1['text']= ""  
def del2():
    texto2['text']= ""  
#comando novo
def novo1():
    texto1['text']= "Novo1" 
    texto2['text']= "Novo2"     
# comando fechar
def fechar():
    jn['text']= quit    

barramenu=Menu(jn)
jn.configure(menu=barramenu)
#barramenu
menuArquivo=Menu(barramenu,tearoff=0)
menuExcluir=Menu(barramenu,tearoff=0)
menuEdit= Menu(barramenu,tearoff=0)

#cascata
#munu Arquivo
barramenu.add_cascade(label="Arquivo", menu=menuArquivo)
menuArquivo.add_command(label="Novo", command=novo1)
menuArquivo.add_separator()
menuArquivo.add_command(label="Fechar", command=quit)
#muno excluir
barramenu.add_cascade(label="Excluir", menu=menuExcluir)
menuExcluir.add_command(label="Excluir1", command=del1)
menuExcluir.add_separator()
menuExcluir.add_command(label="Excluir2",command=del2)
#menu editar
barramenu.add_cascade(label="Editar", menu=menuEdit)
menuEdit.add_command(label="Editar1",command=edit1)
menuEdit.add_separator()
menuEdit.add_command(label="Editar2",command=edit2)

#label texto
texto1=Label(jn, text='texto1')
texto1.pack()
texto2=Label(jn, text='texto2')
texto2.pack()


jn.geometry('600x500')
jn.mainloop()