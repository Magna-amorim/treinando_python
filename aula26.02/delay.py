from tkinter import*
janela=Tk()

def delay():
    etq['text']= 'Aguarde...'
    janela.after(2000, mensagem)
def mensagem(): 
    etq['text']= 'Botão acionado.'  


janela.iconbitmap('icone.ico')
janela.title('Botão Delay')

#etq=Label(janela, text='')
#etq.pack()

btn=Button(janela, text="Aperte aqui!", padx="40", pady="4", command=delay)
btn.pack()


etq=Label(janela, text='Botão acionado', pady=20)
etq.pack()

janela.geometry('600x200')
janela.mainloop()