mairAltura = 0
codMaiorAltura = 0
maiorpeso=0
codmaiorpeso=0

while True:
    
    a=float(input("Digite sua altura: "))
    p=float(input("Digite seu peso: "))
    c=int(input("Digite seu código de aluno: "))
    if c==0:
        break

    else:
        if a > mairAltura:
            mairAltura = a
            codMaiorAltura = c
        print(mairAltura, codMaiorAltura)
        if p > maiorpeso:
            maiorpeso=p
            codmaiorpeso=c
        print(maiorpeso, codmaiorpeso)
    