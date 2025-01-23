#Um professor que sortear um dos seus quatro alunos para apagar o
#quadro. Faça um programa que ajude ele, lendo o nome deles e
#escrevendo o nome do escolhido
from random import choice

aluno1 = input("Escreva o nome do aluno: ")
aluno2 = input("Escreva o nome do aluno: ")
aluno3 = input("Escreva o nome do aluno: ")
aluno4 = input("Escreva o nome do aluno: ")

alunos = [aluno1, aluno2, aluno3, aluno4]
sorteio = choice(alunos)

print(f"Aluno  selecionado: {sorteio}")