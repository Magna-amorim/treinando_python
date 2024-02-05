'''contrua um programa que faça o seguinte calculo um aumento de 15% para um salario de R$ 1000,00.'''
#declaraçaõ de variavel
salario=  1000
aumento=  15
#calculo
resultado= salario + (salario * aumento / 100)
# Primero metodo
print("O aumento é", "R$", resultado)
# segundo
print("O aumento é", "R$", salario + (salario *0.15))

# terceiro
print("O aumento é", "R$", salario + (salario * aumento / 100))



'''Elabore um programa que exiba o lucro de uma empresa.
 Sendo a formula lucro= faturamento - custo'''

#Declaração de variavel
faturamento= 5000
custo= 2600
#calculo
resultado= faturamento - custo

print("O seu lucro é de", "R$", resultado)

