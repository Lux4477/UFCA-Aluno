hora = int(input("Digite a hora (0-23): "))
if 0 <= hora < 6:
    print("Está de madrugada")
elif 6 <= hora < 12:
    print("Está de manhã")
elif 12 <= hora < 18:
    print("Está de tarde")
elif 18 <= hora < 24:
    print("Está de noite")