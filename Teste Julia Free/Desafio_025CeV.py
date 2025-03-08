#Crie um programa que leia o nome de uma pessoa e diga se ela tem
#"SILVA" no nome.


nome = input("Digite seu nome completo: ").strip()

posicao = nome.upper().find("SILVA")
print(posicao)
if posicao > 0:
    print("O seu nome tem 'Silva', igual o meu.")

elif posicao == -1:
   print("Boa! Não tem Silva no nome! KKKK")


# A ideia é fazer o find não encontrar, que ocasionará em -1