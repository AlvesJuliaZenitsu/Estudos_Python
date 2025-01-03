from random import choice

a1 = input("Escreva o nome do aluno: ")
a2 = input("Escreva o nome do aluno: ")
a3 = input("Escreva o nome do aluno: ")
a4 = input("Escreva o nome do aluno: ")

alunos = [a1, a2, a3, a4]
sorteio = choice(alunos)

print(f"Aluno  selecionado: {sorteio}")