import random

def calcular_imposto(valor):
    if valor < 1000:
        imposto = valor * 0.1
    elif valor < 2000:
        imposto = valor * 0.13
    else:
        imposto = valor * 0.2

    return imposto

produto1 = 500
produto2 = 1500
produto3 = 3000

print(f"Valor do imposto para esses produtos são: Produto 1: {calcular_imposto(produto1)} \ Produto 2: {calcular_imposto(produto2)} \  Produto 3: {calcular_imposto(produto3)} ")