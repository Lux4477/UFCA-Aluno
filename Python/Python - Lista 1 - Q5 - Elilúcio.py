import math
x1 = int(input("Escreva o x do primeiro ponto: "))
y1 = int(input("Escreva o y do primeiro ponto: "))
x2 = int(input("Escreva o x do segundo ponto: "))
y2 = int(input("Escreva o y do segundo ponto: "))
d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
if d == 0:
    print("Os pontos são coincidentes.")
else:
    print(f"A distância entre os pontos é {d}.")