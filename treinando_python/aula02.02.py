''' type reconhece o tipo '''
#b= "olá"
#print(b,type(b))

''' Operadores de Atribuição, serve para abreviar uma formula
subtração multiplicação divisão divisão inteira '''

#x=10 #subtraçaõ
#x-=5
#print(x)

#x=10 #multiplicação
#x*=5
#print(x)

''' if '''

#a=int(input("Primeiro valor "))
#b=int(input("Segundo valor "))
#if a>b:
    #print("O primeiro número é o maior")    
#if b>a:
    #print("O segundo número é o maior")

'''
crie um codigo que exiba 
o usuario coloca a idade do carro 
se ele for menor ou igual a 3 de a frase seu carro é novo 
se for maior que 3 seu carro é velho '''

#idade=int(input("Digite a idade do seu carro: "))
#if idade<=3:
    #print("Seu carro é novo")    
#if idade>3:
    #print("Seu carro é velho")

#salario= float(input("Digite o sálario para cálculo do imposto: "))
#base= salario
#imposto =0
#if base >3000:
    #imposto = imposto + ((base- 3000)*0.35)
    #base =3000
#if base >=1000:
    #imposto = imposto +((base - 1000)* 0.20)
#print("salário: R$%6.2f Imposto a pagar: R$%6.2f" % (salario, imposto))

''' Else, '''
    
#idade=int(input("Digite a idade do seu carro: "))
#if idade<=3:
    #print("Seu carro é novo")    
#else:
#print("Seu carro é velho")

#minutos= int(input("minutos utilizados: "))
#if minutos < 200:
   #preco = 0.20
#if minutos < 400:
    #preco = 0.40
#else:
    #preco= 0.18
#print("Voce vai pagar este mes: R$%6.2f" %(minutos * preco))


''' elif é a abreviatura para else if, ou seja se if for falso, 
testa outra condicao antes de else'''

#valor=10
#if valor == 1:
 #   print('a entrada era 1')
#elif valor == 2:
    #print('a entrada era 2')
#elif valor == 3:
    #print('a entrada era 3')
#elif valor == 4:
    #print('a entrada era 4')
#else: 
    #print("o valor de entrada não era esperado")


'''
   operadores lógicos usando and (e) quando true (verdade)
crie um programa simples para saber se uma pessoa pode fazer um financiamento:
requisito necessário
uma renda acima de R$ 5.000,00
seu nome deve estár limpo'''

#renda_acima_5mil = False
#nome_limpo = True

#if renda_acima_5mil and nome_limpo:
    #print('financiamento aprovado')
#else:
    #print('Financiamento Negado')



#renda_acima_5mil = False
#nome_limpo = True

#if renda_acima_5mil or nome_limpo:
    #print('financiamento aprovado')
#else:
    #print('Financiamento Negado')

''' 
   multiplos operadoresde comparação
para cadastrar um produto no e-comerce ele devera custar entre 20 e 40reais
se nao o anuncio nao era aprovado'''

#valor_produto= float(input("Digite o valor do Produto: "))

#if valor_produto >= 20 and valor_produto <40:
    #print("Produto foi aceito")
#else: 
    #print("Produto negado")

#valor = 1
#if 20<= valor <40:
    #print("produto foi aceito")
#else: print("Produto não aceito")

nota1= float(input('Digite sua nota 1º Bimestre: '))
nota2= float(input('Digite sua nota 2º Bimestre: '))
nota3= float(input('Digite sua nota 3º Bimestre: '))
nota4= float(input('Digite sua nota 4º Bimestre: '))
media= ((nota1 + nota2 + nota3 + nota4)/4)

if media >= 6:
    print("Aprovado", "sua nota",media)
if media <3:
    print("Reprovado",media)
else: 
    print("Exame",media)







   



