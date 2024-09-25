Caderno=100
Caneta=100
Lapis=100
Borracha=100
Regua=100

while True:
    print("E-Entrada no Estoque")
    print("S-Saída no Estoque")
    print("R-Relatório")
    print("X-Sair")

    op=input("Digite o código: ")
    
    if op == "E" or op == "e":
        Cod=int(input("Código do produto: "))
        qtd=int(input("Quantidade para da entrada: "))
        if Cod==10:
            Caderno=Caderno+qtd
            print(f"Entrada de {qtd} Cadernos feito com sucesso. Quantidade total {Caderno}")

        if Cod==20:
            Caneta=Caneta+qtd
            print(f"Entrada de {qtd} Caneta feito com sucesso. Quantidade total {Caneta}")
        
        if Cod==30:
            Lapis=Lapis+qtd
            print(f"Entrada de {qtd} Lapis feito com sucesso. Quantidade total {Lapis}")
        if Cod==40:
            Borracha=Borracha+qtd
            print(f"Entrada de {qtd} Borracha feito com sucesso. Quantidade total {Borracha}")
        if Cod==50:
            Regua=Regua+qtd
            print(f"Entrada de {qtd} Regua feito com sucesso. Quantidade total {Regua}")

    elif op == "S" or op=="s":
        Cod=int(input("Código do produto: "))
        qtd=int(input("Quantidade para da saída: "))
        if Cod==10:
            Caderno=Caderno-qtd
            print(f"Saida de {qtd} Cadernos feito com sucesso. Quantidade total {Caderno}")

        if Cod==20:
            Caneta=Caneta-qtd
            print(f"Saida de {qtd} Caneta feito com sucesso. Quantidade total {Caneta}")
        
        if Cod==30:
            Lapis=Lapis-qtd
            print(f"Saida de {qtd} Lapis feito com sucesso. Quantidade total {Lapis}")
        if Cod==40:
            Borracha=Borracha-qtd
            print(f"Saida de {qtd} Borracha feito com sucesso. Quantidade total {Borracha}")
        if Cod==50:
            Regua=Regua-qtd
            print(f"Saida de {qtd} Regua feito com sucesso. Quantidade total {Regua}")
    elif op == "R" or op == "r":
        print(f"Cadernos{Caderno}")
        print(f"Canetas{Caneta}")
        print(f"Lapis{Lapis}")
        print(f"Borracha{Borracha}")
        print(f"Regua{Regua}")

    elif op == "X" or op == "x":
        print("Programa Finalizado!")
        break

    else:
        print("Opção invalida!")