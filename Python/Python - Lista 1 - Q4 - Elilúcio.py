num_1 = float(input("Escreva um número: "))
while True:
    oper = str(input("Digite a operação(+, -, *, /): "))
    if oper in ['+', '-', '*', '/']:
        break
    else:
        print("Operação inválida.")
num_2 = float(input("Escreva outro número: "))
if oper == '+':
    resultado = num_1 + num_2
elif oper == '-':
    resultado = num_1 - num_2
elif oper == '*':
    resultado = num_1 * num_2
elif num_2 == 0:
    print("Erro, divisão por zero não é permitida.")
else:
    resultado = num_1 / num_2
print(f"O resultado será: {resultado}")