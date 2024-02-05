'''loops _ For'''

''' Crie um programa que imprima numeros de 1 a 5'''

#for numero in range(1,6, 2):
    #print(numero)

#for numero in range(1,20, 3):
    #print(numero)
#for numero in range(1,101):
   #print(numero)

'''For utilizando string'''

#palavra= "google"
#for palavra in "Google":
    #print(palavra)

#palavra = "google"
#for letra in palavra:
    #print (f' {letra} esta dentro da palavra Google')

''' Crie um programa que o usuario insira o seu nome e imprima letra po letra seguida de uma frase'''

#nome= str (input("Digite seu nome: "))
#for letra in nome:
    #print (f' {letra} esta dentro do nome', nome)

'''Utilizando for junto com if e else

crie um código de uma loja online, 
com a condição que o cliente recebera uma mensagem de compra "compra no valor de 12,50 
e entrega confirmada" e Detalhes enviado para seu email" ou "falha neacompra".'''

'''com a afirmacao true =  verdadeira'''
#compra_aprovada= True
#dados_compra = 'compra no valor de R$ 12,50 e entrega confirmada'
#for enviar in range(3):
    #if compra_aprovada:
        #print(dados_compra)
    #print('Detalhes enviado por email')
    #break
#else:
    #print('Falha na compra')

'''testando com afirmacao falsa'''
'''compra_aprovada= False
dados_compra = 'compra no valor de R$ 12,50 e entrega confirmada'
for enviar in range(3):
    if compra_aprovada:
        print(dados_compra)
    print('Detalhes enviado por email')
    break
else:
    print('Falha na compra')'''

#criaçao do outer for loop
#for numero1 in range(5):
    #print(numero1)

#criação do inner for loop
    #for numero2 in range(5):
        #print(numero1, numero2)

        
#criaçao do outer for loop
#for numero1 in range(1,6):
    #print('Produto', str(numero1))

#criação do inner for loop
    #for numero2 in range(11):
        #print(numero1, numero2)

'''palavra= "FANTASTICO"
#declaracao for
for spaco in palavra:
    print(spaco)'''

#palavra= "FANTASTICO"
#declaracao for
#for spaco in palavra:
        #print (spaco, end= '  ')

''' o end='' quer dizer que a variavel deve imprimir letra por letra
sem descer uma linha'''

 #ou


#palavra= "FANTASTICO"
#declaracao for
#for spaco in palavra:
    #print(f' {spaco}', end=' ')

#palavra = str (input("Digite uma palavra: "))
#for spaco in palavra: 
    #print(f' {spaco}', end=' ')

'''criação de retangulo 
criando um retangulo de 6x6'''

linhas= 6
colunas= 6 
simbolo= 'x'
for l in range(linhas):
    for c in range(colunas):
        print(simbolo, end = '  ')
    print()    
 