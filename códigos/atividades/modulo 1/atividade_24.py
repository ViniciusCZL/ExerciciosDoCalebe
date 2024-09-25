
numero=int(input("Digite um numero maior que 0: "))
triangular=False
t=0
while t*(t+1)*(t+2)<=numero:
    t=t+1

    if t*(t+1)*(t+2)==numero:
        triangular=True
        break

if triangular==True:
    print("ele é triangular")
else:
    print("ele não é triangular")