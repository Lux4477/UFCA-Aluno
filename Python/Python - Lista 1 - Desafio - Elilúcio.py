letra = str(input("Digite uma letra: ")).upper()
if letra in ['A', 'E', 'I', 'O', 'U']:
    print("A letra é uma vogal.")
elif letra in ['Q', 'W', 'R', 'T', 'Y', 'P', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']:
    print("A letra é uma consoante.")
else:
    print("Entrada inválida.")