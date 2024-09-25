while True:
    x=int(input("informe um numero de 0 a 10: "))
    
    if x<0:
        print(f"Nota inválida.")

    if x>10:
        print("nota inválida.")
    
    else:
        print(f"nota válida.")
        break