# manipulaçao de string/ parte 2
# listas
# funções para manipulaçao de listas
# operações com listas
# tuplas
# dicionarios
# bibliotecas
# funções

'''manipulaçao de string/ parte 2'''

#palavra= "Apostila de Python"

#lower
#print(palavra.lower())
#tudo minusculo

#upper
#print(palavra.upper())
#tudo maiusculo

#swapcase
#print(palavra.swapcase())
#primeira letra minusculo, inverte.

#title
#print(palavra.title())
#as primeiras letras em maiusculo

#split
#print(palavra.split())
#transforma tipo lista de dados

'''fatiamento de strings'''

#s="Python"
#print(s[1:4])

#print(s[2:])

#print(s[:4])

'''Listas '''

#l=[3, "abacate",9.7,[5,6,3],"limão",(3,'j')]
#print(l[2])
#print(l[3])
#print(l[3][1])

'''
para alterar um elemnto da lista basta fazer uma atribuicao de valor atraves do indice. 
o valor existente sera substituido pela nova'''

#l=[3, "abacate",9.7,[5,6,3],"limão",(3,'j')]
#l[3]=str(input("Digite uma palavra ou um número: "))
#print(l)

'''trocar elememnto de uma lista dentro de outra lista'''

#l=[3, "abacate",9.7,[5,6,3],"limão",(3,'j')]
#l[3][1]=str(input("Digite uma palavra ou um número: "))
#print(l)


'''manipulacao de listas'''
#l= [1,2,3,4]
#len
#print(len(l))
#retorna o tamanho da lista

#min
#print(min(l))
#retorna o menor valor da lista

#max
#print(max(l))
#retorna o maior valor da lista

#sum
#print(sum(l))
#retorna a soma dos elementos da lista

#in
#print(3 in l)
#verifica se um valor pertence a lista


#l= [5,7,2,9,4,1,3]
#l.sort()
#print('Lista em ordem crescente:', l)
#l.reverse()
#print("inverte os elemnetos",l )

'''operações com listas'''

#concatenação (+)

#a=[0,1,2]
#b=[3,4,5]
#c=a+b
#print(c)

#Repetição(*)

#l=[1,2]
#r= l*4
#print(r)

#l1 = list(range(5))
#print(l1)

#l2 = list(range(3,8))
#print(l2)

#l3 = list(range(2,11,3))
#print(l3)

'''tupla= seus elementos nao podem ser alterados'''

#t= (1,2,3,4,5)
#print(t)
#resposta (1, 2, 3, 4, 5)

#t=(1,2,3,4,5)
#print(t[3])
#resposta 4

''' desempacotamento de tuplas,
 que permite atribuir os elementos armazenados em uma tuplas a diversas variaveis'''

#t =(10,20,30,40,50)
#a,b,c,d,e = t
#print('a=',a,"b=",b)

'''dicionarios'''

#D={"arroz":17.30, "feijao":12.50,"carne":23.90,"alface":3.40}
#print(D)

#D={"arroz":17.30, "feijao":12.50,"carne":23.90,"alface":3.40}
#print(D["carne"])

''' é possivel acrescentar ou modificar valores no dicionario'''

#D={"arroz":17.30, "feijao":12.50,"carne":23.90,"alface":3.40}
#D["carne"]=25.0
#D["tomate"]=8.80
#print(D)

'''
os valores do dicionario nao possuem ordem
por isso a ordem de impressao dos valores nao é sempre a mesma'''

'''operaçoes em dicionario'''

#Dx={2:"carro", 3:[4,5,6], 7:('a','b'), 4: 173.8}
#print(Dx[7])
#print(Dx[3])
#print(Dx[2])

'''Bibliotecas 
'''
#chama uma biblioteca inteira
#import math
#print(math.factorial(6))

#chama uma funcao especifica da biblioteca
#from math import factorial
#print(factorial(6))

'''Funções'''
'''funcoes sao definidas por uma palavra chave'''
#def hello():
#    print("Ola Mundo!")
#hello()  

'''funcao para imprimir o mair entre 2 valores'''  

#def maior(x,y):
#   if x>y:
#        print(x)
#    else:
#        print(y)
#maior(4,7)

'''escopo de variaves'''

#def soma (x,y):
#    total = x+y
#    print("total soma=",total)
#programa principal
#total =10
#soma(3,5)
#print("Total principal=",total)

'''retorno de valores'''

#def soma (x,y):
#    total = x+y
#    return total
#programa principal
#s=soma(3,5)
#print("soma=",s)

''' Interface graficas'''








