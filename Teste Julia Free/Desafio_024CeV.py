#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não
#com o nome "SANTO"


#LER O NOME DA CIDADE
cidade = str(input("Escreva o nome da cidade: ")).strip()

#vERIFICAR SE COMEÇA COM A PALAVRA SANTO
posicao = cidade.upper().find("SANTO")

if posicao == 0:
    print("O nome da sua cidade começa com Santo")
else:
    print("O nome da sua cidade não começa com Santo")

