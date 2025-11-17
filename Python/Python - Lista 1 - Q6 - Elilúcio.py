import math
x1 = int(input("Escreva o x do primeiro ponto: "))
y1 = int(input("Escreva o y do primeiro ponto: "))
x2 = int(input("Escreva o x do segundo ponto: "))
y2 = int(input("Escreva o y do segundo ponto: "))
x3 = int(input("Escreva o x do terceiro ponto: "))
y3 = int(input("Escreva o y do terceiro ponto: "))
lado1 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
lado2 = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
lado3 = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2:
    print("Os pontos formam um triângulo.")
else:
    print("Os pontos não formam um triângulo")