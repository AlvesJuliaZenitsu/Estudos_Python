from math import cos, sin, tan, radians

angulo = int(input("Digite o valor de um angulo: "))
convertido = radians(angulo)
print(f"O seno do angulo inserido é {sin(convertido):.2}, o coseno é {cos(convertido):.2} e a tangente é {tan(convertido):.2}")

