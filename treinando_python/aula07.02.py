'''While '''
''' Exemplo usando while'''
#contador= 2
#while contador<6:
#   print(f'valor do contador é {contador}')
#  contador -= 1

#resp = input('Deseja iniciar o programa? s/n')
#while resp != "s" and resp != "n":
    #resp= input('resposta invalida!!! continuar? s/n?')
    #print('resposta ok. Vamos continuar o programa')
    #print('Fim do programa')


''' Exemplo usando while'''
#n= int (input("Digite um número para ser somado:[999 - para parar] "))
#soma = 0
#while n!= 999:
#    soma+= n
#   n= int(input("Digitr outro numero para ser somado com os anteriores: 999 - para sair "))
#    print("soma = {}".format(soma))

''' Exemplo usando while'''

#senha = "54321"
#leitura = " "
#while (leitura != senha):
#    leitura = input("Digite a senha: ")
#    if leitura == senha:
#        print("Acesso liberado")
#    else:
#        print("Senha incorreta. Tente novamente")  

'''
Fibonacci:
O exempolo abaixo imprime a sequencia de Fibonacci até a quantidade  
de termos informada pelo usuario'''

#qtde = int(input("Quantos termos de fibonacci você deseja?"))
#anterior = 0
#atual = 1
#contador = 1

#while contador <= qtde:
#    print('{}-' .format (atual), end = '  ') 
#    proximo = anterior + atual
#   anterior = atual
#   atual = proximo
#  contador += 1
#   print(contador)
#print ("Fim do programa de Fibonacci")
        
'''
o programa abaixo soma diversos numeros digitados pelo usuario. 
Este programa exibe a soma calculada e tambem qual foi o menor e maior números digitados'''

'''
soma = 0
qtdenumeros = 1
resp = 's'
while resp == 's':
    n = int(input("Digite um numero: "))
    if qtdenumeros == 1:
        maior = n
        menor = n 
        maior = n  
    if n < menor:
        menor = n   
    soma += n
    resp = input('deseja continuar digitando? s / n ')
    while resp != 's' and resp != 'n':
        resp = input ('informe se deseja continuar digitando: s / n ')
    if resp == 's':
        qtdenumeros += 1
print("quantidade de numeros somados: {}" .format(qtdenumeros))
print(f'soma = {soma}')
print(f'menor número entre os digitados foi {menor}')
print(f'maior número entre os digitados foi {maior}')
'''

'''
soma= cont = 0
while True:
    n =int (input("Digite um número: "))
    if n == 999:
        break
    cont =+ 1
    soma += n
print(f'você somou {cont} numeros')
print(f'a soma de todos foi {soma}')
'''

# par ou impar, com o computador. o programa deve terminar qaundo o computador vencer o usuario
# quando terminar mostre quantas partdas o usuario venceu

'''
import random
ptsusuario = ptscomputador = 0
while True:
    n = int(input("Qual numero entre 0 e 10? "))
    parouimpar = input("par ou impar? responda, p / i: "  )
    while parouimpar != 'p' and parouimpar != 'i':
        parouimpar = input('Resposta invalida? Responda: p/i')
    computador = random.randint(0,10)
    soma = n + computador
    if soma %2 == 0 and parouimpar == 'p':
        ptsusuario += 1
    elif soma %2 == 1 and parouimpar == 'i':
        ptsusuario =+1
    else:
        ptscomputador += ptscomputador
        break
print(f'Você venceu {ptsusuario} partidas')
'''

# Escreve um programa que leia um número de 1 a 10,
# e mostre a tabuada desse número.
'''
numero= int(input("Digite um numero entre 0 e 10."))
for i in range(1,11):
    print(numero,"x",i," = ",numero*i,"\n ")
    '''

#num=int(input("Tabuada do número? " ))
#for n in range (0,11):
    #print(f'{num} x {n} = {num*n}')

''' Ou '''

#numero=int(input("digite um numero: "))
#for sequencia in range (1,11):
    #print ("%2d x %2d = %3d" %(numero,sequencia,numero*sequencia))

'''
Manipular string

'''

palavra = "Apostila de Python"

#len()
print(len(palavra))

#capitalize
print(palavra.capitalize())

#count
print(palavra.count("o"))

#startswhith
print(palavra.startswith("Ap"))

#endswhit
print(palavra.endswith("py"))

#isalnum
print(palavra.isalnum())


