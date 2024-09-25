
while True:
    total=0.00
    nproduto=1
    while True:
        produto=float(input("valor do produto: "))
        if produto==0:
            break

        else:
            total+=produto
            nproduto+=1
    print(f"Total:R${total}")

    pagamento=float(input("Dinheiro recebido:R$ "))
    troco=pagamento-total
    print(f"Troco:R${troco}")

    