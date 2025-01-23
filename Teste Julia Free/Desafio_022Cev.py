#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas;
#O nome com todas as letras minúsculas;
#Quantas letras ao todo (sem considerar espaços)
#Quantas letras tem o primeiro nome

nome = input("Digite seu nome completo: ")
sem_espacos = nome.strip()
#mostrar em capslock
print(sem_espacos.upper())

#mostrar todas as letras minusculas
print(sem_espacos.lower())

# quatidade de letras sem mostrar os espaços

print("Quantidade de letras:",len(sem_espacos))

#quantas letras tem o primeito nome
quantiade_nome = sem_espacos.split()
print(f"Seu primeiro nome é {quantiade_nome[0]} e ele tem {len(quantiade_nome[0])} letras")
