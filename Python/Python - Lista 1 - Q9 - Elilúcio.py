while True:
    try:
        T = str(input("Digite a escala de temperatura a ser inserida(C/F/K): ")).upper()
        if T in ['C', 'F', 'K']:
         TC = str(input("Digite a escala de temperatura a ser convertida(C/F/K): ")).upper()
         if TC in ['C', 'F', 'K']:
            if T == TC:
               print("As escalas são iguais, não há conversão a ser feita.")
            else:
               break
        else:
         print("Escala inválida.")
    except ValueError:
       print("Entrada inválida.")
       continue
if T == 'C':
    temp = float(input("Digite a temperatura: "))
    if TC == 'F':
        print(f"Temperatura em Fahrenheit será: {temp * 9 / 5 + 32}")
    if TC == 'K':
      print(f"Temperatura em Kelvin será: {temp + 273}")
elif T == 'F':
    temp = float(input("Digite a temperatura:"))
    if TC == 'C':
       print(f"Temperatura em Celsius será: {(temp - 32) * 5 / 9}")
    if TC == 'K':
        print(f"Temperatura em Kelvin será: {(temp -32)* 5 / 9 + 273}")
else:
    temp = float(input("Digite a temperatura: "))
    if TC == 'C':
     print(f"Temperatura em Celsius será: {temp - 273}")
    if TC == 'F':
      print(f"Temperatura em Fahrenheit será: {(temp - 273) * 9 / 5 + 32}")