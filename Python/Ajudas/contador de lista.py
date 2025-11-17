lista = [int(input("Digite números inteiros: ")) for x in range(10)]
print(len([x for x in lista if x % 2 == 0]))