data = input("digita a data ai:")
if data[2] == "/" and data[5] == "/":
    dia = int(data[0:2])
    mes = int(data[3:5])
    ano = int(data[6:])
    if (dia<=0 or dia >=32) or (mes<=0 or mes>=13) or (ano<=0 or ano>9999):
        print("data invalida")
    else:
        print("data valida")
else:
    print("data invalida")