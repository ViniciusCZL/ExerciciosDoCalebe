class filme:
    def __init__(self,nome,duracao):
        self.nome=nome
        self.duracao=duracao

    def Play(self):
        print(f"O filme",self.nome,"Começou, duração",self.duracao)

        
class ação(filme):
    def __init__(self,nome,duracao):
        super().__init__(nome,duracao)

    def explodir():
        print("Booooom!!")
        

class Drama(filme):
    def __init__(self,nome,duracao):
        super().__init__(nome,duracao)
    
    def aflicao():
        print("estou aflito. :/")

class suspense(filme):
    def __init__(self,nome,duracao):
        super().__init__(nome,duracao)

    def terror():
        print("estou aterrorizado. :o")


filme1 = ação("Transformes",310)
filme2 = Drama("7 Vidas",210)
filme3 = suspense("Sem Limites",220)

while True:
    print("Digite o numero da lista do filme que deseja assistir: ")
    print("[1]Transformes")
    print("[2]7 Vidas")
    print("[3]Sem limites")

    op=int(input("Digite o número aqui: "))
    if op==1:
        filme1.Play()
    
    elif op==2:
        filme2.Play()

    elif op==3:
        filme3.Play()