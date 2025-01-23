#Escreva um programa que converta uma temperatura digitada em °C e a
# converta para °F

celsius = float(input("Insira a temperatura em C°: "))
f = celsius * 1.8 + 32

print(f"A temperatura de {celsius}°C, corresponde a {f}°F")