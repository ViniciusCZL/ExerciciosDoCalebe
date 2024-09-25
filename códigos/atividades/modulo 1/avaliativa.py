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

carrinho_nome_produto=[]
carrinho_valor_produto=[]
carrinho_qtd_produto=[]



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
                                print("####################################")
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
                                        print("####################################")
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
                                        print("####################################")
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
                                            print("####################################")
                                            break
                                    
                                    else:
                                        op3==3
                                        print("####################################")
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
                                    print(carrinho)
                                    print(subtotal)
                                    print("digite o nome do produto que deseja remover, para sair digite somento o numero [9].")
                                    rem=input("Qual produto deseja retirar?")
                                    qtd=int(input("Quantidade que deseja remover: "))
                                    
                                    if rem=="Sabonete Francis 90g" or rem=="sabonete francis 90g" or rem=="SABONETE FRANCIS 90G" or rem=="SABONETE FRANCIS":
                                        carrinho.remove("Sabonete Francis 90g")
                                        x=Sabonete_Francis_90g*qtd
                                        subtotal=subtotal-x
                                        qtd_Sabonete_Francis_90g=qtd_Sabonete_Francis_90g+qtd
                                    
                                    elif rem=="Shampoo Tresemme 400ml" or rem=="shampoo tresemme 400ml" or rem=="shampoo tresemme" or rem=="SHAMPOO TRESEMME":
                                        carrinho.remove("Shampoo Tresemme 400ml")
                                        x=Shampoo_Tresemme_400ml*qtd
                                        subtotal=subtotal-x
                                        qtd_Sabonete_Francis_90g=qtd_Sabonete_Francis_90g+qtd

                                    elif rem=="Condicionador Tresemme 400ml" or rem=="condicionador tresemme 400ml" or rem=="CONDICIONADOR TRESEMME 400ML" or rem=="CONDICIONADOR TRESEMME" or rem=="condicionador tresemme":
                                        carrinho.remove("Condicionador Tresemme 400ml")
                                        x=Condicionador_Tresemme_400ml*qtd
                                        subtotal=subtotal-x
                                        qtd_Sabonete_Francis_90g=qtd_Sabonete_Francis_90g+qtd

                                    elif rem=="Steak" or rem=="STEAK" or rem=="SteaK" or rem=="steak":
                                        carrinho.remove("Steak")
                                        x=steak*qtd
                                        subtotal=subtotal-x
                                        qtd_steak=qtd_steak+qtd

                                    elif rem=="Nuggets Frango Congelado" or rem=="Nuggets Frango Congelado 1.5kg" or rem=="nuggets frango congelado 1.5kg" or rem=="nuggets" or rem=="NUGGETS FRANGO CONGELADO 1.5KG":
                                        carrinho.remove("Condicionador Tresemme 400ml")
                                        x=nuggets_Frango_congelado_1_5kg_*qtd
                                        subtotal=subtotal-x
                                        qtd_nuggets_Frango_congelado_1_5k_=qtd_nuggets_Frango_congelado_1_5k_+qtd

                                    elif rem=="Picanha" or rem=="PICANHA" or rem=="pICANHA":
                                        carrinho.remove("Picanha")
                                        x=Picanha_1kg*qtd
                                        subtotal=subtotal-x
                                        qtd_Picanha_1kg=qtd_Picanha_1kg+qtd

                                    elif rem=="Coca-Cola 2L" or rem=="COCA COLA 2L" or rem=="coca cola 2l" or rem=="coca" or rem=="COCA":
                                        carrinho.remove("Coca-Cola 2L")
                                        x=Cocacola_2l*qtd
                                        subtotal=subtotal-x
                                        qtd_Cocacola_2l=qtd_Cocacola_2l+qtd
                                        
                                    elif rem=="Budweiser 330ml" or rem=="BUDWEISER" or rem=="budweiser" or rem=="budweiser 330ml" or rem=="BUDWEISER 330ML":
                                        carrinho.remove("Budweiser 330ml")
                                        x=Budweiser_330ml*qtd
                                        subtotal=subtotal-x
                                        qtd_Budweiser_330ml=qtd_Budweiser_330ml+qtd

                                    elif rem=="Heineken 330ml" or rem=="HEINEKEN" or rem=="heineken" or rem=="heineken 330ml" or rem=="HEINEKEN 330ML":
                                        carrinho.remove("Heineken 330ml")
                                        x=Heineken_330ml*qtd
                                        subtotal=subtotal-x
                                        qtd_Heineken_330ml=qtd_Heineken_330ml+qtd

                                    elif rem=="Brahma 330ml" or rem=="BRAHMA" or rem=="brahma" or rem=="brahma 330ml" or rem=="BRAHMA 330ML":
                                        carrinho.remove("Brahma 330ml")
                                        x=Brahma_330ml*qtd
                                        subtotal=subtotal-x
                                        qtd_Brahma_330ml=qtd_Brahma_330ml+qtd
                                    
                                    else:
                                        rem==9
                                        print("####################################")
                                        break
                        elif op=="s" or op=="S":
                            print("Compra Cancelada")
                            break

                        elif op=="F" or op=="f":
                            print("[1] PIX")
                            print("[2] Cartão de Crédito")
                            print("[3] Cartão de Débito")
                            print("[4] Dinheiro")
                            print("[5] Voltar")
                            pay=int(input("Digite o número referente a sua forma de pagamento: "))

                            if pay==5:
                                print("Voltando")
                                print("#########")
                                break
                            while True:
                                if pay==1:
                                    IN=subtotal*0.05
                                    IE=subtotal*0.08
                                    IM=subtotal*0.12
                                    Total=subtotal+IN+IE+IM
                                    print(f"valor de imposto nacional{IN}")
                                    print(f"valor de imposto estadual{IE}")
                                    print(f"valor de imposto municipal{IM}")
                                    print(f"Valor total{Total}")
                                    print (f"sei la o que coloca nesse slk")
                                    print (f"deposita nessa chave [05248009103] esse valor {Total} :D ")
                                    print("Pagamento realizado!!!")
                                    break
                                if pay==2:
                                    print ("[1] á vista")
                                    print ("[2] 2 vezes")
                                    print ("[3] 3 vezes")
                                    print ("[4] 6 vezes")
                                    print ("[5] Voltar")
                                    p=int(input("Digite em quantas vezes deseja fazer o pagamento"))

                                    if p==1:
                                        print("Pagamento á vista selecionado!")
                                        print("Aproxime ou Insira o Cartão")
                                        print("Pago")
                                        print("###############")
                                        print (f"Compra Finalizada")
                                        print (carrinho)
                                        print (f"RS{subtotal}")
                                        IN=subtotal*0.05
                                        IE=subtotal*0.08
                                        IM=subtotal*0.12
                                        Total=subtotal+IN+IE+IM
                                        print(f"valor de imposto nacional{IN}")
                                        print(f"valor de imposto estadual{IE}")
                                        print(f"valor de imposto municipal{IM}")
                                        print(f"Valor total{Total}")
                                        break

                                    elif p==2:
                                        print("Pagamento parcelado em 2 selecionado!")
                                        print("Aproxime ou Insira o Cartão")
                                        print("Pago")
                                        print("###############")
                                        print (f"Compra Finalizada")
                                        print (carrinho)
                                        print (f"RS{subtotal}")
                                        IN=subtotal*0.05
                                        IE=subtotal*0.08
                                        IM=subtotal*0.12
                                        Total=subtotal+IN+IE+IM
                                        print(f"valor de imposto nacional{IN}")
                                        print(f"valor de imposto estadual{IE}")
                                        print(f"valor de imposto municipal{IM}")
                                        print(f"Valor total{Total}")
                                        break 
                            
                                    elif p==3:
                                        print("Pagamento parcelado em 3 selecionado!")
                                        print("Aproxime ou Insira o Cartão")
                                        print("Pago")
                                        print("###############")
                                        print (f"Compra Finalizada")
                                        print (carrinho)
                                        print (f"RS{subtotal}")
                                        IN=subtotal*0.05
                                        IE=subtotal*0.08
                                        IM=subtotal*0.12
                                        Total=subtotal+IN+IE+IM
                                        print(f"valor de imposto nacional{IN}")
                                        print(f"valor de imposto estadual{IE}")
                                        print(f"valor de imposto municipal{IM}")
                                        print(f"Valor total{Total}")
                                        break 
                            
                                    elif p==4:
                                        print("Pagamento parcelado em 6 selecionado!")
                                        print("Aproxime ou Insira o Cartão")
                                        print("Pago")
                                        print("###############")
                                        print (f"Compra Finalizada")
                                        print (carrinho)
                                        print (f"RS{subtotal}")
                                        IN=subtotal*0.05
                                        IE=subtotal*0.08
                                        IM=subtotal*0.12
                                        Total=subtotal+IN+IE+IM
                                        print(f"valor de imposto nacional{IN}")
                                        print(f"valor de imposto estadual{IE}")
                                        print(f"valor de imposto municipal{IM}")
                                        print(f"Valor total{Total}")
                                        break

                                    elif p==5:
                                        print("Operação cancelada")
                                        break

                                if pay==3:
                                    print (f"RS{subtotal}")
                                    print ("Insira ou Aproxime o Cartão!")
                                    print ("senha [1]")
                                    con=int(input("digite sua senha: "))
                                    if con==1:
                                        print("Pago")
                                        print("###############")
                                        print (f"Compra Finalizada")
                                        print (carrinho)
                                        print (f"RS{subtotal}")
                                        print ("Volte sempre!!")
                                        IN=subtotal*0.05
                                        IE=subtotal*0.08
                                        IM=subtotal*0.12
                                        Total=subtotal+IN+IE+IM
                                        print(f"valor de imposto nacional{IN}")
                                        print(f"valor de imposto estadual{IE}")
                                        print(f"valor de imposto municipal{IM}")
                                        print(f"Valor total{Total}")
                                        break
                                    
                                if pay==4:
                                    print ("forma de pagamento selecionado em dinheiro.")
                                    IN=subtotal*0.05
                                    IE=subtotal*0.08
                                    IM=subtotal*0.12
                                    Total=subtotal+IN+IE+IM
                                    print(f"valor de imposto nacional{IN}")
                                    print(f"valor de imposto estadual{IE}")
                                    print(f"valor de imposto municipal{IM}")
                                    print(f"Valor total{Total}")
                                    troco=dinheiro-Total
                                    print (f"Total da Compra R${Total}")
                                    dinheiro=float(input("Informe o Valor em dinheiro entregue pelo cliente: "))
                                    
                                    if troco<0:
                                        print("Valor insuficiente")

                                    elif troco>0:
                                        print(f"Troco para o cliente de R${troco}")

                                    elif troco==0:
                                        print(f"Não há necessidade de troco, valor certo. Compra finalizada.")

    elif op == "F" or op == "f":
        
        print("Bem vindo, funcionário!")

        
        produtos_alimentos = [
            {"nome": "Steak", "preço": steak},
            {"nome": "Nuggets Frango Congelado 1.5kg", "preço": nuggets_Frango_congelado_1_5kg_},
            {"nome": "Picanha 1kg", "preço": Picanha_1kg},
            {"nome": "Coca-cola 2l", "preço": Cocacola_2l},
            {"nome": "Budweiser 330ml", "preço": Budweiser_330ml},
            {"nome": "Budweiser 330ml", "preço": Brahma_330ml},
            {"nome": "Heineken 330ml", "preço": Heineken_330ml},
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
                
                while True:
                    if M==matricula or N==nome or D==data_nascimento or C==cpf:

                        print(f"Boas Vindas {nome}")
                        print("[1] Consultar Estoque")
                        print("[2] Atualizar Estoque")
                        print("[3] Adicionar Novos Produtos")
                        print("[4] Voltar")
                        op_0=int(input("Digite o que deseja fazer: "))
                        if op_0==4:
                            break
                        while True:
                            if op_0==1:
                                print(f"Brahma{qtd_Brahma_330ml},Budweiser{qtd_Budweiser_330ml},Heinken{qtd_Heineken_330ml}, Coca-Cola 2L{qtd_Cocacola_2l}, Picanha{qtd_Picanha_1kg}, Nuggets{qtd_nuggets_Frango_congelado_1_5k_}, Steak{qtd_steak}, Condicionador Tresemme 400ml{qtd_Condicionador_Tresemme_400ml}, Shampoo Tresemme{qtd_Shampoo_Tresemme_400ml}, Sabonete Francis 90g{qtd_Sabonete_Francis_90g}")
                                break
                            
                            elif op_0==2:
                                print("[1] Entrada de Produto")
                                print("[2] Saída de Produto")
                                print("[3] Atualizar Preço do Produto")
                                print("[4] Voltar")
                                op_1=int(input("Digite a opção que deseja: "))

                                if op_1==4:
                                    print("############")
                                    break

                                while True:
                                    if op_1==1:
                                        print("digite o numero a esquerda para ir a seção que deseja")
                                        print("[1] Higiene")
                                        print("[2] Alimentos")
                                        print("[3] Bebidas")
                                        print("[4] Sair")
                                        print("-------------------ATENÇÃO----------------")
                                        print("AS OPÇÕES [2] E [3] NÃO ESTÃO ATIVDADAS, PARA EXEMPLO DO EXERCICIO DEIXEI APENAS O [1] ATIVADO E [4] PARA SAIR.")

                                        op_2=int(input("Digite aqui: "))

                                        if op_2 == 4:
                                            print("####################################")
                                            break

                                        while True:
                                            if op_2==1:

                                                print("digite o número a esquerda para selecionar o subtipo.")
                                                print("[1] Sabonte")
                                                print("[2] Shampoos")
                                                print("[3] Condicionadores")
                                                print("[4] Voltar")
                                                op_3=int(input("Digite aqui: "))

                                                if op_3==1:
                                                    print(f"[1] Sabonete Francis 90g{qtd_Sabonete_Francis_90g}")
                                                    op_4=int(input("Digite qual produto deseja da entrada de mercadoria: "))
                                                    op_5=int(input("Digite a quantidade que deseja fazer entrada:"))
                                                    if op_4==1:
                                                        qtd_Sabonete_Francis_90g=qtd_Sabonete_Francis_90g+op_5
                                                        break

                                                elif op_3==2:
                                                    print(f"[1] Shampoo Tresemme 400ml{qtd_Shampoo_Tresemme_400ml}")
                                                    op_4=int(input("Digite qual produto deseja da entrada de mercadoria: "))
                                                    op_5=int(input("Digite a quantidade que deseja fazer entrada:"))
                                                    if op_4==1:
                                                        qtd_Shampoo_Tresemme_400ml=qtd_Shampoo_Tresemme_400ml+op_5
                                                        break

                                                elif op_3==3:
                                                    print(f"[1] Condicionador Tresemme 400ml {qtd_Condicionador_Tresemme_400ml}")
                                                    op_4=int(input("Digite qual produto deseja da entrada de mercadoria: "))
                                                    op_5=int(input("Digite a quantidade que deseja fazer entrada:"))
                                                    if op_4==1:
                                                        qtd_Condicionador_Tresemme_400ml=qtd_Condicionador_Tresemme_400ml+op_5
                                                        break

                                                elif op_3==4:
                                                    break
                                while True:
                                    if op_1==3:
                                        print("digite o numero a esquerda para ir a seção que deseja")
                                        print("[1] Higiene")
                                        print("[2] Alimentos")
                                        print("[3] Bebidas")
                                        print("[4] Sair")
                                        print("-------------------ATENÇÃO----------------")
                                        print("AS OPÇÕES [2] E [3] NÃO ESTÃO ATIVDADAS, PARA EXEMPLO DO EXERCICIO DEIXEI APENAS O [1] ATIVADO E [4] PARA SAIR.")

                                        op_2=int(input("Digite aqui: "))

                                        if op_2 == 4:
                                            print("####################################")
                                            break

                                        while True:
                                            if op_2==1:

                                                print("digite o número a esquerda para selecionar o subtipo.")
                                                print("[1] Sabonte")
                                                print("[2] Shampoos")
                                                print("[3] Condicionadores")
                                                print("[4] Voltar")
                                                op_3=int(input("Digite aqui: "))

                                                if op_3==1:
                                                    print(f"[1] Sabonete Francis 90g - R${Sabonete_Francis_90g}")
                                                    op_4=int(input("Digite qual produto deseja atualizar o valor de venda: "))
                                                    op_5=float(input("Digite o novo valor do produto: "))
                                                    if op_4==1:
                                                        Sabonete_Francis_90g=Sabonete_Francis_90g-Sabonete_Francis_90g+op_5
                                                        print(f"Novo Valor modificado, no valor de R${Sabonete_Francis_90g}")
                                                        break

                                                elif op_3==2:
                                                    print(f"[1] Shampoo Tresemme 400ml - R${Shampoo_Tresemme_400ml}")
                                                    op_4=int(input("Digite qual produto deseja atualizar o valor de venda: "))
                                                    op_5=float(input("Digite o novo valor do produto: "))
                                                    if op_4==1:
                                                        Shampoo_Tresemme_400ml=Shampoo_Tresemme_400ml-Shampoo_Tresemme_400ml+op_5
                                                        print(f"Novo Valor modificado, no valor de R${Shampoo_Tresemme_400ml}")
                                                        break

                                                elif op_3==3:
                                                    print(f"[1] Condicionador Tresemme 400ml - R${Condicionador_Tresemme_400ml}")
                                                    op_4=int(input("Digite qual produto deseja atualizar o valor de venda: "))
                                                    op_5=float(input("Digite o novo valor do produto: "))
                                                    if op_4==1:
                                                        Condicionador_Tresemme_400ml=Condicionador_Tresemme_400ml-Condicionador_Tresemme_400ml+op_5
                                                        break

                                                elif op_3==4:
                                                    break
                            elif op_0==3:
                                print("adicionar novo produto")
                                nproduto=input("Digite o nome do novo produto: ")
                                vproduto=input("Digite o valor do novo produto: ")
                                qtdproduto=input("Digite a quantidade do novo produto que deseja adicionar ao estoque: ")

                                carrinho_nome_produto.append(nproduto)
                                carrinho_valor_produto.append(vproduto)
                                carrinho_qtd_produto.append(qtdproduto)

                                print(carrinho_nome_produto)
                                print(carrinho_valor_produto)
                                print(carrinho_qtd_produto)
                                break