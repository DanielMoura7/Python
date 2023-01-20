usuário = input("Qual o seu usuário? ")
senha = input("Qual a sua senha?")

usuário_bd = "arthur_abcd"
senha_bd = "08056466550"

if usuário == usuário_bd and senha == senha_bd:
    print("Você esta logado")
else:
    print("Usuário ou Senha inválidos")