#criação de janela
import tkinter
Window= tkinter.Tk()
#criacao da função def
def novo():
    text_area.delete(1.0, "end")
def abrir():
    file=open("notepad.txt", "r")
    container=file.read()
    text_area.insert(1.0, container)
def salvar():
   container=text_area.get(1.0, "end")
   file=open("notepad.txt", "w")
   file.write(container)
   file.close()
#def update
def update():
    font=spin_font.get()
    size=spin_size.get()
    text_area.config(font="{} {}". format(font, size))   

#criaçao de titulo
Window.title("Notpade")
#definiçao do tamanho minimo de tela
Window.minsize(width=1208, height=720)

#barra de feramenta
frame=tkinter.Frame(Window, height=30)
frame.pack(fill="x")

#tipo de fonte
fonte_text=tkinter.Label(frame,text="Fonte")
fonte_text.pack(side="left")

#spinbox
spin_font=tkinter.Spinbox(frame, values=("Arial", "Verdana","jokerman",
                                         "Constantia","Engravers MT",))
spin_font.pack(side="left")

#tamanho da fonte
fonte_size=tkinter.Label(frame,text="Fonte Size")
fonte_size.pack(side="left")

#spinbox2
spin_size=tkinter.Spinbox(frame, from_=0, to=60)
spin_size.pack(side= "left")

#criacao de botao update
btn=tkinter.Button(frame, text='Up', command=update)
btn.pack(side="left")

#criação de area de texto
text_area=tkinter.Text(Window, font="Arial 20 bold", width=1200, height=800)
text_area.pack()

#criacao de menu
main_menu=tkinter.Menu(Window)
arquivo_menu= tkinter.Menu(main_menu, tearoff=0)
arquivo_menu.add_command(label='Novo', command=novo)
arquivo_menu.add_command(label='Abrir', command=abrir)
arquivo_menu.add_command(label='Salvar', command=salvar)
arquivo_menu.add_command(label='Fechar', command=Window.quit)
main_menu.add_cascade(label='Arquivo', menu=arquivo_menu)

Window.config(menu=main_menu)
#definiçao do tamanho minimo de tela
Window.minsize(width=800, height=120)
#Window.geometry('500x600')
#final do programa
Window.mainloop()