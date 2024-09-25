numero=int(input("Digite um numero maior que 0: "))
t=0
while t*(t+1)*(t+2)<numero:
    t=t+1

if t*(t+1)*(t+2)==numero:
    print(f"o numero {numero} é triangular {t,t+1,t+2}")
    
elif t*(t+1)*(t+2)!=numero:
    print(f"o numero {numero} não é triangular.")
    
else:
    print("não é valido")
        