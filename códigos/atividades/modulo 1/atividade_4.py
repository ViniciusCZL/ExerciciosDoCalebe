a = int(input("Olá  digite qual é o valor de {A}"))

b = int(input(" me informe o valor de {B}"))

c = int(input("por fim o valor de {C}"))


if a==0:
    print ("a equação não é do segundo grau e o programa não deve pedir demais valores, sendo encerrado")
else:

    delta = (b**2) - (4*a*c)
    if(delta < 0):
      print("Não possue raiz real")

    if(delta == 0):
      x1 = -b  / (2*a)
      y1= (a*x1)**2*(x1+b)*(x1+c)
      print(f"valor de delta é igual a 0 possui apenas uma raiz resultando em x igual a {x1} e y igual a {y1}")

    else :
       x2 = (-b+(delta**0.5))/(2*a)
       x3 = (-b-(delta**0.5))/(2*a)

     
y2= ((a*x2)**2)+(b*x2)+(c)


V=((-b/(2*a))*(-delta/(4*a)))

print (f"valor de x1 {x2} é  e de x2 {x3} valor de y é {y2} e o a vértice é {V}")

