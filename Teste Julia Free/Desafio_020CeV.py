#Um professor que sortear a ordem de apresentação de trabalhos
#dos alunos. Faça um programa que leia o nome dos quatro alunos e
#mostre a ordem sorteada.

from random import sample

aluno1 = input("Escreva o nome do aluno: ")
aluno2 = input("Escreva o nome do aluno: ")
aluno3 = input("Escreva o nome do aluno: ")
aluno4 = input("Escreva o nome do aluno: ")

alunos = [aluno1, aluno2, aluno3, aluno4]
sorteio = sample(alunos, k=4)

print(f"Ordem sorteada: {sorteio}")

#com o shuffle, o código vai embaralhar a lista inteira.
# Utilizando o sample, você passa um parametro da quantidade dos elementos que você
# quer sortear, e evita repetições.