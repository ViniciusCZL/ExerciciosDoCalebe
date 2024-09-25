#sua leitura estava fora do while, ai ele não estava atualizando os numero e ficando em loop infinito
soma=0
while True:
    num= input() #coloquei a leitura aqui
    if num != '0':
        while num!='':
            soma= soma + int(num[0])
            num=num[1:]
    elif num == '0':
        print(soma)
        break
    else:
        print("invalido")