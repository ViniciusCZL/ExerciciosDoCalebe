class Notas():
    Nome=""
    RA=""
    N1=0
    N2=0
    N3=0
    N4=0

    def inserirDados(self):
        self.Nome=(input("Insira o nome do aluno: "))
        self.RA=(input("Digite o RA do Aluno: "))
        self.N1=float(input("Digite a nota do primeiro bimestre do aluno: "))
        self.N2=float(input("Digite a nota do segundo bimestre do aluno: "))
        self.N3=float(input("Digite a nota do terceiro bimestre do aluno: "))
        self.N4=float(input("Digite a nota do quarto bimestre do aluno: "))
        
    def media(self):
        soma=self.N1+self.N2+self.N3+self.N4
        med=soma/4
        if med<=5:
            print(med)
            print("reprovado")
        
        elif med<=6.9:
            print(med)
            print("Exame")

        else:
            print(med)
            print("aprovado")

    def situacao(self):
        print(f"Situação do aluno",self.Nome)
        print(f"RA do aluno",self.RA)
        print(f"Nota 1B",self.N1)
        print(f"Nota 2B",self.N2)
        print(f"Nota 3B",self.N3)
        print(f"Nota 4B",self.N4)
        self.media()

nota=Notas()

def mostrarMenu():
    print("MENU")
    print("(1) Inserir Dados.")
    print("(2) Mostrar situação")
    print("(3) Sair.")

mostrarMenu()

while True:
    op=int(input("Digite a opção que deseja: "))

    if op==1:
        nota.inserirDados()

    elif op==2:
        nota.situacao()

    elif op==3:
        print("Finalizado.")
        break