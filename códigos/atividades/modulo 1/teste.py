Sabonete_Francis_90g=4.70
Shampoo_Tresemme_400ml=18.00
Condicionador_Tresemme_400ml=23.00
steak=0.75
nuggets_Frango_congelado_1_5kg_=20.00
Picanha_1kg=58.99
Cocacola_2l= 8.89
Budweiser_330ml=4.00
Heineken_330ml=4.00
Brahma_330ml=2.50

qtd_Sabonete_Francis_90g=100
qtd_Shampoo_Tresemme_400ml=100
qtd_Condicionador_Tresemme_400ml=100
qtd_steak=100
qtd_nuggets_Frango_congelado_1_5k_=100
qtd_Picanha_1kg=100.00
qtd_Cocacola_2l= 100
qtd_Budweiser_330ml=100
qtd_Heineken_330ml=100
qtd_Brahma_330ml=100



carrinho=[]
subtotal=0

nome = ""
cpf = ""


while True:
    print("Selecione a opção abaixo:")
    print("[C] Cliente")
    print("[F] Funcionário")

    op = input("Digite aqui: ")

    if op == "C" or op == "c":
        print("Bem vindo, cliente!")
        while True:
            print("[1] Entrar")
            print("[2] Fazer cadastro")

            op_c = int(input("Digite aqui: "))

            if op_c == 2:
                c1 = input("Digite seu nome : ")
                c3 = input("Digite seu CPF sem caracteres: ")

                nome = c1
                cpf = c3

                print("Cadastro realizado")

            elif op_c == 1:
                N1 = input("Digite seu nome: ")
                C1 = input("Digite seu CPF sem caracteres: ")
                nome==N1
                cpf==C1

                while True:
                    print("Boas vindas ao vini produtor!!")
                    print("Digite [c] caso queira adicionar ao carrinho!")
                    print("Digite [r] caso queira retirar do carrinho!")
                    print("Digite [f] caso queira finalizar a compra!")
                    print("Digite [s] caso queira cancelar a compra!")

                    op=input("digite aqui: ")

                    while True:
                        if op=="c" or op=="C":

                            print("digite o numero a esquerda para ir a seção que deseja")
                            print("[1] Higiene")
                            print("[2] Alimentos")
                            print("[3] Bebidas")
                            print("[4] Sair")
                            op2=int(input("Digite aqui: "))

                            if op2 == 4:
                                break

                            while True:
                                if op2==1:

                                    print("digite o número a esquerda para selecionar o subtipo.")
                                    print("[1] Sabonte")
                                    print("[2] Shampoos")
                                    print("[3] Condicionadores")
                                    print("[4] Voltar")
                                    op3=int(input("Digite aqui: "))

                                    if op3==1:

                                        print("digite o produto que deseja adicionar ao carrinho e em seguida quantidade!")
                                        print("[1] Sabonte Francis 90g - R$4,70")
                                        op4=int(input("digite o produto que deseja adiocionar ao carrinho."))
                                            
                                        if op4==1:
                                            carrinho.append("Sabonete Francis 90g")
                                            op5=float(input("digite a quantidade que deseja: "))
                                            x=Sabonete_Francis_90g*op5
                                            qtd_Sabonete_Francis_90g=qtd_Sabonete_Francis_90g-op5
                                            subtotal=subtotal+x
                                            print(subtotal)
                                            
                                    if op3==2:

                                        print("digite o produto que deseja adicionar ao carrinho e em seguida quantidade!")
                                        print("[1] Shampoo Tresemme 400ml - R$18.00")
                                        op4=int(input("digite o produto que deseja adiocionar ao carrinho."))
                                            
                                        if op4==1:
                                            carrinho.append("Shampoo Tresemme 400ml")
                                            op5=float(input("digite a quantidade que deseja: "))
                                            x=Shampoo_Tresemme_400ml*op5
                                            qtd_Shampoo_Tresemme_400ml=qtd_Shampoo_Tresemme_400ml-op5
                                            subtotal=subtotal+x
                                            print(subtotal)
                                    if op3==3:

                                        print("digite o produto que deseja adicionar ao carrinho e em seguida quantidade!")
                                        print("[1] Shampoo Tresemme 400ml - R$18.00")
                                        op4=int(input("digite o produto que deseja adiocionar ao carrinho."))
                                            
                                        if op4==1:
                                            carrinho.append("Condicionador Tresemme 400ml")
                                            op5=float(input("digite a quantidade que deseja: "))
                                            x=Condicionador_Tresemme_400ml*op5
                                            qtd_Condicionador_Tresemme_400ml=qtd_Condicionador_Tresemme_400ml-op5
                                            subtotal=subtotal+x
                                            print(subtotal)
                                            
                                    else:
                                        op3==4
                                        break
                                
                                elif op2==2:
                                    print("digite o número a esquerda para selecionar o subtipo.")
                                    print("[1] Frios")
                                    print("[2] Carne")
                                    print("[3] Voltar")
                                    op3=int(input("Digite aqui: "))

                                    if op3==1:

                                        print("digite o produto que deseja adicionar ao carrinho e em seguida quantidade!")
                                        print("[1] Steak - R$0,75")
                                        print("[2] Nuggets Frango Cong/ 1.5kg")
                                        op4=int(input("digite o produto que deseja adiocionar ao carrinho."))
                                            
                                        if op4==1:
                                            carrinho.append("Steak")
                                            op5=float(input("digite a quantidade que deseja: "))
                                            x=steak*op5
                                            qtd_steak=qtd_steak-op5
                                            subtotal=subtotal+x
                                            print(subtotal)

                                        elif op4==2:
                                            carrinho.append("Nuggets Frango Congelado 1.5kg")
                                            op5=float(input("digite a quantidade que deseja: "))
                                            x=nuggets_Frango_congelado_1_5kg_*op5
                                            qtd_nuggets_Frango_congelado_1_5k_=qtd_nuggets_Frango_congelado_1_5k_-op5
                                            subtotal=subtotal+x
                                            print(subtotal)                                            
                                    
                                    elif op3==2:
                                        print("digite o produto que deseja adicionar ao carrinho e em seguida quantidade!")
                                        print("[1] Picanha - R$58,99")
                                        op4=int(input("digite o produto que deseja adiocionar ao carrinho: "))
                                        if op4==1:
                                            carrinho.append("Picanha")
                                            op5=float(input("digite a quantidade que deseja: "))
                                            x=Picanha_1kg*op5
                                            qtd_Picanha_1kg=qtd_Picanha_1kg-op5
                                            subtotal=subtotal+x
                                            print(subtotal)
                                    
                                    else:
                                        op3==3
                                        break

                                elif op2==3:

                                    print("digite o número a esquerda para selecionar o subtipo.")
                                    print("[1] Refrigerantes")
                                    print("[2] Cervejas")
                                    print("[3] Voltar")
                                    op3=int(input("Digite aqui: "))

                                    if op3==1:
                                        print("digite o produto que deseja adicionar ao carrinho e em seguida quantidade!")
                                        print("[1] Coca-Cola 2L - R$8,89")
                                        op4=int(input("Digite o produto que deseja adicionar ao carrinho: "))
                                        if op4==1:
                                            carrinho.append("Coca-Cola 2L")
                                            op5=int(input("Digite a quantidade que deseja: "))
                                            x=Cocacola_2l*op5
                                            qtd_Cocacola_2l=qtd_Cocacola_2l-op5
                                            subtotal=subtotal+x
                                            print(subtotal)

                                    elif op3==2:
                                        print("digite o produto que deseja adicionar ao carrinho e em seguida quantidade!")
                                        print("[1] Budweiser 330ml - R$4,00 ")
                                        print("[2] Heineken 330ml - R$4,00 ")
                                        print("[3] Brahma 330ml - R$2,50")
                                        print("[4] Voltar")
                                        op4=int(input("Digite o produto que deseja adicionar ao carrinho: "))
                                        if op4==1:
                                            carrinho.append("Budweiser 330ml")
                                            op5=int(input("Digite a quantidade que deseja: "))
                                            x=Budweiser_330ml*op5
                                            qtd_Budweiser_330ml=qtd_Budweiser_330ml-op5
                                            subtotal=subtotal+x
                                            print(subtotal)

                                        elif op4==2:
                                            carrinho.append("Heineken 330ml")
                                            op5=int(input("Digite a quantidade que deseja: "))
                                            x=Heineken_330ml*op5
                                            qtd_Heineken_330ml=qtd_Heineken_330ml-op5
                                            subtotal=subtotal+x
                                            print(subtotal)
                                            
                                        elif op4==3:
                                            carrinho.append("Brahma 330ml")
                                            op5=int(input("Digite a quantidade que deseja: "))
                                            x=Brahma_330ml*op5
                                            qtd_Brahma_330ml=qtd_Brahma_330ml-op5
                                            subtotal=subtotal+x
                                            print(subtotal)

                                        else:
                                            op4==4
                                            break
                                    
                                    else:
                                        op3==3
                                        break
                    
                        
                        elif op=="r" or op=="R":
                            print(carrinho)
                            print("digite o opção abaixo.")
                            print("[1] Retirar produto do carrinho.")
                            print("[2] voltar.")
                            
                            op2=int(input("Digite aqui: "))

                            if op2==2:
                                break

                            while True:                            
                                if op2==1:

                                    rem=input("Qual produto deseja retirar?")
                                    qtd=int(input("Quantidade que deseja remover: "))
                                    
                                    if rem=="Sabonete Francis 90g" or rem=="sabonete francis 90g" or rem=="SABONETE FRANCIS 90G" or rem=="SABONETE FRANCIS":
                                        carrinho.remove("Sabonete Francis 90g")
                                        x=Sabonete_Francis_90g*qtd
                                        subtotal=subtotal-x
                                        qtd_Sabonete_Francis_90g=qtd_Sabonete_Francis_90g+qtd
                                    
                                    elif rem=="Shampoo Tresemme 400ml" or rem=="shampoo tresemme 400ml" or rem=="shampoo tresemme" or rem=="SHAMPOO TRESEMME":
                                        carrinho.remove("Shampoo Tresemme 400ml")
                                    
                                        subtotal=subtotal-qtd
                                        qtd_Sabonete_Francis_90g=qtd_Sabonete_Francis_90g+qtd

                                    elif rem=="Condicionador Tresemme 400ml" or rem=="condicionador tresemme 400ml" or rem=="CONDICIONADOR TRESEMME 400ML" or rem=="CONDICIONADOR TRESEMME" or rem=="condicionador tresemme":
                                        carrinho.remove("Condicionador Tresemme 400ml")
                                        subtotal=subtotal-qtd
                                        qtd_Sabonete_Francis_90g=qtd_Sabonete_Francis_90g+qtd

                            


    elif op == "F" or op == "f":
        
        print("Bem vindo, funcionário!")

        
        produtos_alimentos = [
            {"nome": "Steak", "preco": steak},
            {"nome": "Nuggets Frango Congelado 1.5kg", "preco": nuggets_Frango_congelado_1_5kg_},
            {"nome": "Picanha 1kg", "preco": Picanha_1kg},
            {"nome": "Coca-cola 2l", "preco": Cocacola_2l},
            {"nome": "Budweiser 330ml", "preco": Budweiser_330ml}
        ]

        produtos_higiene = [{"nome": "Sabonete Francis 90g", "preco": Sabonete_Francis_90g},
            {"nome": "Shampoo Tresemme 400ml", "preco": Shampoo_Tresemme_400ml},
            {"nome": "Condicionador Tresemme 400ml", "preco": Condicionador_Tresemme_400ml}]

        matricula = ""
        nome = ""
        data_nascimento = ""
        cpf = ""


        while True:
            print("[1] Entrar")
            print("[2] Fazer cadastro")

            op_f = int(input("Digite aqui: "))

            if op_f == 2:
                print("Sua matrícula é: 123")
                c1 = input("Digite seu nome : ")
                c2 = input("Digite sua data de nascimento sem caracteres: ")
                c3 = input("Digite seu CPF sem caracteres: ")

                matricula = "123"
                nome = c1
                data_nascimento = c2
                cpf = c3

                print("Cadastro realizado")

            elif op_f == 1:
                M = input("Digite sua matrícula sem caracteres: ")
                N = input("Digite seu nome: ")
                D = input("Digite sua data de nascimento sem caracteres: ")
                C = input("Digite seu CPF sem caracteres: ")


# if carrinho == Budweiser_330ml:
#     for i in carrinho.remove(Budweiser_330ml):
