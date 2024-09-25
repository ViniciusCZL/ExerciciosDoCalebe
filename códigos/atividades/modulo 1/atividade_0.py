x=float(input("digite o salário:"))
if x<500:
    reajuste=x*0.15+x
elif x<1000:
    reajuste=x*0.10+x
else:
    reajuste=x*0.05+x
print (f"o reajuste do salario sera de {reajuste}")