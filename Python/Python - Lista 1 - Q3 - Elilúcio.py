ligar = False
while ligar == False:
    lig = str(input("Ligar a máquina? (L/l): "))
    if lig == "L" or lig == "l":
        ligar = True
        print("Máquina ligada.")
    else:
        print("Erro, um comando inválido foi inserido.")
while ligar == True:
    com = str(input("Digite o que deseja fazer, desligar ou furar (D/d ou F/f): "))
    if com == "F" or com == "f":
        print("Furando...")
    elif com == "D" or com == "d":
        ligar = False
        print("Máquina desligada.")
    else:
        print("Erro, um comando inválido foi inserido.")