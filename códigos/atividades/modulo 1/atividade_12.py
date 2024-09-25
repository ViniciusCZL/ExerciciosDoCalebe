# Sistema de cadastro de usuários

usuario1_nome = "alice"
usuario1_senha = "1234"

usuario2_nome = "bob"
usuario2_senha = "abcd"

usuario3_nome = "carol"
usuario3_senha = "9876"
print("Bem-vindo ao sistema de cadastro de usuários!")

opcao = int(input("Escolha uma opção - 1: Login, 2: Cadastro:"))

if opcao == 1: 
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    if (usuario == usuario1_nome and senha == usuario1_senha) or (usuario == usuario2_nome and senha == usuario2_senha) or (usuario == usuario3_nome and senha == usuario3_senha):
        print("Login bem-sucedido!")
    else:
        print("Nome de usuário ou senha incorretos!")
elif opcao == 2:
    print("Cadastre-se") 
    while True:

        novo_usuario_nome = input("Digite seu novo nome de usuário: ")
        novo_usuario_senha = input("Digite sua nova senha: ")
        if novo_usuario_nome==novo_usuario_senha:
            print("Cadastro invalido nome e senha iguais!")

            print("Faça seu cadastro novamente!")
        else:
            print("cadastro feito com sucesso!")
            print("Obrigado!")
            break