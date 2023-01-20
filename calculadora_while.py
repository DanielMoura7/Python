while True:
    print()
    num1 = input("Digite um Número! ")
    num2 = input("Digite Outro Número! ")
    operador = input("Digite um Operador: + - / * ")
    sair = input("Deseja sair da calculadora? Se sim, digite: s ")

    if sair == 's':
        break

    if not num1.isnumeric() or not num2.isnumeric():
        print("Você precisa digitar um número! ")
        continue

    num1 = int(num1)
    num2 = int(num2)

    if operador == '+':
        print(num1 + num2)
    elif operador == '-':
        print(num1 - num2)
    elif operador == '/':
        print(num1 / num2)
    elif operador == '*':
        print(num1 * num2)
    else:
        print("Operador inválido")