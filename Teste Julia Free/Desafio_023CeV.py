#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um
#dos digitos separados

# 1° TENTATIVA COMO STRING, NÃO É EFICIENTE, vide correção em "23matematica"

numero = input("Digite um numero: ")
dividido = numero.split()



print("Unidade:", dividido[0][3])
print("Dezena:", dividido[0][2])
print("Centena:", dividido[0][1])
print("Milhar:", dividido[0][0])

