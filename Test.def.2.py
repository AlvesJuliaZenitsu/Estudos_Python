
def primitivo(algo):

    print("O tipo primitivo é:", type(numero_inserido))
    print("É um numero?!", numero_inserido.isnumeric())
    print("É alfabetico?", numero_inserido.isalpha())
    print("É alfanumerico?", numero_inserido.isalnum())
    print("Esta maiusculo?", numero_inserido.isupper())
    print("Esta minusculoo?", numero_inserido.islower())
    print("Esta capitalizada?", numero_inserido.istitle())
    return

numero_inserido = input("Digite algo: ")