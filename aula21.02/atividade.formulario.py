from tkinter import *
janela = Tk()

def selecao():
    nome=entrada1.get()
    if var1.get() ==1:
        x='Python'
    else:
        x=" "    
    if var2.get() ==1:
        y="Java"    
    else:
        y=" " 
    if var3.get() ==1:   
        z="C#"   
    else:
        z=" "
    if var.get() ==1:
        w="Masculino" 
    if var.get() ==2:  
        w="Feminino" 
        etq5['text'] = nome + "  " + w +' ' + lista.get(ANCHOR) + "  " +  x  +  y  +  z


etq1=Label(janela, text=' Qual o seu nome?')
etq1.pack()

entrada1=Entry(janela, width=50,)
entrada1.pack()

etq2=Label(janela, text=' Qual o sexo?', pady=15)
etq2.pack()

#radiobutton
var= IntVar()
rb1= Radiobutton(janela, text= 'Masculino', variable=var, value=1)
rb1.pack()
rb2= Radiobutton(janela, text= 'Feminino', variable=var, value=2)
rb2.pack()

etq3=Label(janela, text=' Qual a unidade do seu curso?', pady=15)
etq3.pack()

#listebox frame com scrolbar
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

etq4=Label(janela, text=' Qual o curso?', pady=15)
etq4.pack()

#checkbox
frame2= Frame (janela, pady=15)
frame2.pack()

var1= IntVar()
cb1= Checkbutton(frame2, text= 'Python', variable=var1)
cb1.pack(anchor = 'w')

var2= IntVar()
cb2= Checkbutton(frame2, text= 'Java', variable=var2)
cb2.pack(anchor = 'w')

var3= IntVar()
cb3= Checkbutton(frame2, text= 'C#', variable=var3)
cb3.pack(anchor = 'w')

#botao selecionar
btn=Button(janela, text='Selecionar',  padx='10', pady='2.5',command=selecao)
btn.pack()

#etiqueta de resposta
etq5=Label(janela, text=' ', pady=15)
etq5.pack()

janela.geometry('500x600+50+200')
janela.mainloop()