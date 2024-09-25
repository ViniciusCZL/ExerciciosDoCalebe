while True:
    total=0
    contador=0
    produto=float(input("valor do produto: "))
    if produto==0:
        print("total: ", total)
        dinheiro=float(input("dinheiro: "))
        print("dinheiro:", dinheiro)
        print("troco:", (dinheiro-total))
        break