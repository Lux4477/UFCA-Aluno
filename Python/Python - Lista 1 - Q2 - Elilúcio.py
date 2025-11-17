num_1 = int(input("escreva um número inteiro(1/3): "))
num_2 = int(input("escreva um número inteiro(2/3): "))
num_3 = int(input("escreva um número inteiro(3/3): "))
if num_1 > num_2:
    if num_1 > num_3:
        print(f"o maior número é {num_1}")
    else:
        print(f"o maior número é {num_3}")
elif num_2 > num_3:
    print(f"o maior número é {num_2}")
else:
    print(f"o maior número é {num_3}")