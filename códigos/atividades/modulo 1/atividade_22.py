c1=0
c2=0
c3=0
c4=0
n=0
b=0

while True:
    voto=int(input("digite o codigo do voto ou 0 para encerrar"))
    if voto==0:
        break
    elif voto==1:
        c1=c1+1
    elif voto==2:
        c2=c2+1
    elif voto==3:
        c3=c3+1
    elif voto==4:
        c4=c4+1
    elif voto==5:
        n=n+1
    elif voto==6:
        b=b+1
    else:
        print("Valor Invalido!")

print(f"votos no c1 {c1}, votos no c2 {c2}, votos no c3 {c3}, votos no c4 {c4}, votos no n {n}, votos no b {b}")