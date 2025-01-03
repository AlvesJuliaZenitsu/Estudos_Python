from random import sample

a1 = input("Escreva o nome do aluno: ")
a2 = input("Escreva o nome do aluno: ")
a3 = input("Escreva o nome do aluno: ")
a4 = input("Escreva o nome do aluno: ")

alunos = [a1, a2, a3, a4]
sorteio = sample(alunos, k=4)

print(f"Ordem sorteada: {sorteio}")

#com o shuffle, o código vai embaralhar a lista inteira.
# Utilizando o sample, você passa um parametro da quantidade dos elementos que você
# quer sortear, e evita repetições.