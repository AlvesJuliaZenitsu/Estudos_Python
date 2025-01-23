#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
# com 5% de desconto.


produto = float(input("Insira o valor do produto: R$"))
total = produto - (produto * 0.05)

print(f"O Valor total com desconto é R${total:.2f}")