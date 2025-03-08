#Faça um programa que leia o nome completo de uma pessoa, mostrando
# em seguida o primeiro e o último nome separadamente.


nome = input("Escreva seu nome completo: ").strip()


dividido = nome.split()

print("Primeiro =", dividido[0])

print("Último =", dividido[-1])