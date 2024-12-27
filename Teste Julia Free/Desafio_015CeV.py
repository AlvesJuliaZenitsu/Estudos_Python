
dias = int(input("Quantos dias alugado? "))

kmrodado = float(input("Quantos Km rodados? "))

total = (60 * dias) + (0.15 * kmrodado)
print(f"O total a pagar é de R${total:2}")

