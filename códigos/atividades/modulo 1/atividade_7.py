while True:
    print("menu:")
    print("1 Multiplicaçao")
    print("2 Divisao")
    print("3 Adisao")
    print("4 Subtraçao")
    print("5 Sair")
    
    l = int(input("escolha a operaçao"))

    if l == 5:
        print("ok")
        break
    else:

        x=float(input("digite o primeiro número: "))
        y=float(input("digite o primeiro número: "))


    if l==2:
        x=x/y
        print(x)
    else:
        if l==1:
            x=x*y
            print(x)
        else:
            if l==3:
                x=x+y
                print(x)
            else:
                l==4
                x=x-y
                print(x)
                