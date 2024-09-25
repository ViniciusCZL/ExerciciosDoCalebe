class conta():
    def __init__(self, nome,cpf ,numero , saldo):
        self.nome=nome
        self.cpf=cpf
        self.saldo=saldo
        self.numero=numero
    
    def mostrar(self):
        print(self.nome)
        print(self.cpf)
        print(self.numero)
        print(self.saldo)
        
    def deposito(self):
        self.saldo=float(input("\ndigite o valor do deposito: "))    
    
    def sacar(self):
        self.saldo=self.saldo-(float(input("\ndigite o valor que deseja sacar: ")))
        
    def mostrarS(self):
        print(self.saldo)

while True:
    p1 = str(input("\n digite seu nome: "))
    p2 =int(input("digite seu cpf: "))
    break

t1 = conta(p1 , p2 , 2 , 0.0)


while True:
    
    print("\n(1) informações ")
    print("(2) depositar ")
    print("(3) sacar ")
    print("(4) imprimir saldo")
    print("(5) Sair")
    
    op1 = int(input("\n digite aqui: "))
    
    if op1 == 1:
        t1.mostrar()
        
    
    if op1 == 2:
        t1.deposito()
        
    elif op1==3:
        t1.sacar()
        
    elif op1==4:
        t1.mostrarS()
    
    else:
        op1==5
        print("finalizado.")
        break

class triangulo:
    nome="vinicius"
    sobrenome="lopes"
    horastra=0.0
    valorhora=0.0

    def horatrabalho(self):
        self.horastra=float(input("Digite a quantidade de horas trabalhada: "))

    def valor(self):
        self.valorhora=float(input("Digite o valor da hora de trabalho: "))
        
t=triangulo()

print(t.nome,t.sobrenome)

