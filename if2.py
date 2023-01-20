horario = int(input("Escreva a hora atual em valores de 00 - 24 hrs "))

if horario <= 12:
    print("Bom dia!")
elif horario <= 18:
    print("Boa Tarde!")
else:
    print("Boa noite!")