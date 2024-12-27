largura = float(input("Insira a largura da parede: "))
altura = float(input("Insira a altura da parede: "))
area = largura * altura

qtd_tinta = area/2
print(f"A área da parede é de {area}m^2, e você precisará de {qtd_tinta} litros de tinta para pintá-la")