print("digite a operação que deseja, conforme os numeros abaixos: ")
print("1.multiplicação")
print("2.divisão")
print("3.subtração")
print("4.adição")
print("5.sair")


while True:
    
    x=int(input("digite aqui: "))
    if x==5:
        print(" finalizado ")
        break
    n1=int(input("digite o primeiro numero da operação: "))
    n2=int(input("digite o segundo numero da operação: "))
    
    if x==1:
        m=n1*n2
        print(m)

    elif x==2:
        d=n1/n2
        print(d)

    elif x==3:
        s=n1-n2
        print(s)
    
    elif x==4:
        a=n1+n2
        print(a)
    
    elif x==5:
        print(" finalizado ")
        break