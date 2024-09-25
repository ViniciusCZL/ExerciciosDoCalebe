login="vinicius"
senha="senhafoda123"

while True:
    x=input("digite seu login: ")
    y=input("digite seu senha: ")
    if x==login and y==senha:
        print("logado")
        break
    if x==y:
        print("erro digite novamente")