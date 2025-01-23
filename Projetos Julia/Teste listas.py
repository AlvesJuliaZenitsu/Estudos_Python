fruta = ['maça', 'banana', 'pera']

novaf = input("Escreva a fruta que deseja adicionar:  ")
fruta.append(novaf)
print(fruta)
if novaf in fruta:
    print(f"A {novaf} está na lista!")

fruta.sort()
print(fruta)
