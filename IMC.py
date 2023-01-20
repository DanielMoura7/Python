nome = "Daniel Moura"
idade = 21
altura = 1.78
peso = 92
ano = 2023
nascimento = ano - idade
imc = peso / altura**2

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso} kgs.')
print(f'O IMC de {nome} é {imc:.2f}')
print(f'{nome} nasceu em {nascimento}')