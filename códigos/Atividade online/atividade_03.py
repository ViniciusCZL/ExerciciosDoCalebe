salario=float(input("digite seu salário: "))
prestacao=float(input("digite a prestação que deseja: "))
limite = salario * 0.20
if prestacao>limite:
    print("prestação negada, maior que o limite de 20% do salario")
else:
    print("prestação permitida, fazendo empréstimo")
