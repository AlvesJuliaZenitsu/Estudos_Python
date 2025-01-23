#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um
#dos digitos separados

numero = int(input("Digite um numero: "))

unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero// 100) % 10
milhar = (numero // 1000) % 10
print(f" A unidade é: {unidade}")
print(f" A dezena é: {dezena}")
print(f" A centena é: {centena}")
print(f" A milhar é: {milhar}")