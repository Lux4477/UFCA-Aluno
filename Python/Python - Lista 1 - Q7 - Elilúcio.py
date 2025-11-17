lado1 = int(input("Digite o comprimento de um lado do triângulo(1/3): "))
lado2 = int(input("Digite o comprimento de um lado do triângulo(2/3): "))
lado3 = int(input("Digite o comprimento de um lado do triângulo(3/3): "))
if lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    if lado1 == lado2 and lado2 == lado3:
        print("O triângulo é equilátero")
    else:
        print("O triângulo é isósceles")
else:
    print("O triângulo é escaleno")