x=int(input("Digite o valor da nota "))
while True:
 if x>10 or x<0:
  print("nota inválida, digite novamente")
  x=int(input("Digite o valor da nota "))
 elif x<=10 and x>=0:
  print("Nota válida")
  break