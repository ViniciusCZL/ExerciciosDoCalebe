class Pessoa:
    Nome=["Vinícius Lopes"]
    Idade=0
    Endereço=["Rua Serra Azul,244"]

    def mostrarNome(self):
        print(self.Nome)
    
    def Alteraridade(self):
        self.Idade=int(input("Digite a nova idade: "))
        
    def imprimirEndereço(self):
        print(self.Endereço)

    def mostrarIdade(self):
        print(self.Idade)


def MostrarMenu():
    print("________Menu_________")
    print("___[1]Mostrar Nome___")
    print("___[2]Alterar Idade__")
    print("_[3]Imprimir Endereço")
    print("___[4]Mostrar Idade__")
while True:
    MostrarMenu()

    op=int(input("Digite uma opção: "))
    x=Pessoa()
    if op==1:
        x.mostrarNome()
        
    elif op==2:
        x.Alteraridade()

    elif op==3:
        x.imprimirEndereço()

    elif op==4:
        x.mostrarIdade()

    else:
        print("Comando Invalido")