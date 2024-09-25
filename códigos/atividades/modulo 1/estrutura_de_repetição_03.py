while True:
    x=str(input("Digite seu nome: "))

    if x==x[0:3]:
        print("caracteres insuficientes, digite novamente!")

    else:
        print(f"Nome aceito Sr.(Sra.) {x}")
    
    y=int(input("Digite a idade acima de 0:"))

    if y>=0 or y<=150:
        print(f"Idade válida")

