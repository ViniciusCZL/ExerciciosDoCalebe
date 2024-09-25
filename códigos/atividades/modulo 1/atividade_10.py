n = input("Digite um numero menor que 1000")

if(int(n) > 1000):
    print("Numero invalido")
else:
    if(int(n) >= 100):
        cent = int(n[0])
        deze = int(n[1])
        uni = int(n[2])
        centText = "centenas"
        dezeText = "Dezenas"
        uniText = "Unidades"

        if(cent == 1):
            centText = "Centena"
        if(deze == 1):
            dezeText = "Dezena"
        if(uni == 1):
            uniText = "Unidade"
        
        print(f"{n} = {cent} {centText}, {deze} {dezeText} e {uni} {uniText}")
    elif(int(n) >= 10 and int(n) < 99 ):
        deze = int(n[0])
        uni = int(n[1])
        dezeText = "Dezenas"
        uniText = "Unidades"
        if(deze == 1):
            dezeText = "Dezena"
        if(uni == 1):
            uniText = "Unidade"
        
        print(f"{n} = {deze} {dezeText} e {uni} {uniText}")
    else:
        uni = int(n)
        uniText = "Unidades"

        if(uni == 1):
            uniText = "Unidade"
        print(f"{n} = {uni} {uniText}")