vlr = float(input("Digite o  valor: "))
if vlr < 100:
    print(f"O valor inflacionado será: R${vlr * 1.1}")
else:
    print(f"O valor inflacionado será: R${vlr * 1.2}")