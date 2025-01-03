from math import pow, sqrt, hypot

#qual é o cateto oposto
cat_op = float(input("Digite o valor do cateto oposto: "))
#qual é o adjacente
cat_ad = float(input("Digite o valor do cateto adjacente: "))
#calcular e mostrar a hipotenusa
#hip = pow(cat_op, 2) + pow(cat_ad, 2)
hip = hypot(cat_op, cat_ad)
print(f"O valor da hipotenusa é {(hip):.3}")