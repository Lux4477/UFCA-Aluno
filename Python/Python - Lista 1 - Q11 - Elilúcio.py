th = int(input("Digite quantas horas você ficou no estacionamento: "))
tm = int(input("Digite quantos minutos você ficou no estacionamento: "))
th = th + tm / 60
if th <= 1:
    valor = th * 2
elif th > 1 and th <= 2:
    valor = 2 + (th - 1) * 1.5
elif th > 2:
    valor = 3.5 + (th - 2)
print(f"O valor a ser pago pela estadia é R${valor:.2f}")