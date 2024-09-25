class carro:
    marca = "ford"
    modelo = "mustang"
    km= 141321.1
    ano=1983
    status="Parado"

    def EngineMotor(self):
        self.status ="Ligado"
        print(self.status)

    def offmotor(self):
        self.status="Desligado"
        print(self.status)

    def Movimentar(self):
        self.status="Em movimento"
        self.km+=0.0001    
        print(self.status)
    
    def Parar(self):
        self.status="Parado"
        print(self.status)

def menu():
    print("Menu")
    print("[1]Ligar Veículo.")
    print("[2]Desligar Veículo.")
    print("[3]Andar com o Veículo.")
    print("[4]Parar Veículo.")


op2=carro()
while True:
    menu()
    op=int(input("Digite aqui a função que deseja fazer com o carro."))
    if op==1:
        op2.EngineMotor()
        
    elif op==2:
        op2.offmotor()
        
    elif op==3:
        op2.Movimentar()
        
    elif op==4:
        op2.Parar()
        
    else:
        break