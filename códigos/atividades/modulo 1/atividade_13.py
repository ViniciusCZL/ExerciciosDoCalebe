while True:
    x=str(input("Digite seu nome: "))

    if x==x[0:3]:
        print("caracteres insuficientes, digite novamente!")

    else:
        print("sucesso")
        break

while True:
    idade=int(input("digite sua idade: "))

    if idade<=0 or idade>150:
        print("idade não é válida!Digite novamente.")

    else:
        print("Idade válida")
        break

while True:
    salário=int(input("Digite seu salário: "))

    if salário<=0:
        print("Valor do salário inválido, digite novamente!!")

    else:
        print("Sucesso!")
        break

while True:
    Sexo=str(input("Digite seu genero. [f] feminino [m] masculino [o] outros: "))
    if Sexo=="f" or Sexo=="m" or Sexo=="o":
        print("sucesso!")
        break

    else:
        print("valor invalido, tente novamente!")
    
while True:
    EC=str(input("digite seu estado civil: [s] para solteiro [c] casado [v] viuvo [d] divorciado"))

    if EC=="s" or EC=="c" or EC=="d" or EC=="v":
        print("sucesso, valor valido!")
        break

    else:
        print("valor invalido, tente novamente!")
    
        