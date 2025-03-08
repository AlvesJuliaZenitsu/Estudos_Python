# Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A";
#Em que posição ela aparece a primeira vez;
# Em que posição ela aparece a última vez
from tokenize import endpats



frase = input("Escreva uma frase bem feliz: ")

print(f" A letra 'A' aparece {frase.upper().count('A')} vezes")

#print(frase.split())

print(f" A letra A aparece a primeira vez na {(frase.upper().find('A')) + 1}° posição")

print(f" O caractere aparece por último na {(frase.upper().rfind('A')) + 1}° posição")
