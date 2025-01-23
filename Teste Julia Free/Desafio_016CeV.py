#Crie um programa que leia um número Real qualquer pelo teclado
# e mostre na tela a sua porção inteira.


from math import trunc

num = float(input("Insira um número real: "))

print(f"O número digitado em sua porção inteira é: {trunc(num)}")