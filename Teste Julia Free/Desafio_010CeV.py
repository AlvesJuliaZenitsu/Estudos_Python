#Crie um programa que leia quanto dinheiro  uma pessoa tem na carteira
# e mostre quantos Dólares ela pode comprar.

# Considere: US$1,00 = R$3,27      (;-; dolar ja foi 3 reais... )


n1 = float(input("Digite quantos reais você tem na carteira: "))


compra_dolar = n1//3.27

print(f"Com R${n1}, você pode comprar {compra_dolar} dolares")

