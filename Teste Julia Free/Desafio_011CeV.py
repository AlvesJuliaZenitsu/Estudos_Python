#Faça um programa qur leia a largura e a altura de uma parede
# em metros, calcule a sua área e a quantidade de tinta necessária
# para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m^2.


largura = float(input("Insira a largura da parede: "))
altura = float(input("Insira a altura da parede: "))
area = largura * altura

quantidade_tinta = area/2
print(f"A área da parede é de {area}m^2, e você precisará de {quantidade_tinta} litros de tinta para pintá-la")