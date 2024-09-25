import random

from avaliativa_02 import bingo

sorteio=[]
class Bingo_Sorteio:
    def numero(self):
        numero=random.randint(1,75)
        if not numero in sorteio:
                sorteio.append(numero)
                print()
                print()
                print(numero)
                print()
                print()
                return numero
    
        else:
            self.numero()

    def menu(self,cartela):
        while True:
            print("[1] sortear numero.")
            print("[3] parar.")
            x=int(input("Digite a opção"))
            if x==1:
                self.verificar(cartela)
            
            elif x==3:
                break

            elif x==2:
                print(novoBingo.tabela())
            
            elif x==4:
                self.verificar(cartela)
    
    def verificar(self,cartela):

        marcador=int(input("digite o numero marcado: "))

        for i in range(len(cartela.B)):
            
            if marcador == cartela.B[i]:
                cartela.B[i]=0

        for i in range(len(cartela.I)):
            if marcador == cartela.I[i]:
                cartela.I[i]=0

        for i in range(len(cartela.N)):
            if marcador == cartela.N[i]:
                cartela.N[i]=0

        for i in range(len(cartela.G)):
            if marcador == cartela.G[i]:
                cartela.G[i]=0

        for i in range(len(cartela.O)):
            if marcador == cartela.O[i]:
                cartela.O[i]=0

        if cartela.B[0]==0 and cartela.B[1]==0 and cartela.B[2]==0 and cartela.B[3]==0 and cartela.B[4]==0:
            print("Bingo! Na linha [B]")

        elif cartela.B[0]==0 and cartela.I[0]==0 and cartela.N[0]==0 and cartela.G[0]==0 and cartela.O[0]==0:
            print("Bingo!! Na coluna [1]")

        elif cartela.I[0]==0 and cartela.I[1]==0 and cartela.I[2]==0 and cartela.I[3]==0 and cartela.I[4]==0:
            print("Bingo! Na linha [I]")

        elif cartela.B[1]==0 and cartela.I[1]==0 and cartela.N[1]==0 and cartela.G[1]==0 and cartela.O[1]==0:
            print("Bingo!! Na coluna [2]")

        elif cartela.N[0]==0 and cartela.N[1]==0 and cartela.N[2]==0 and cartela.N[3]==0:
            print("Bingo! Na linha [N]")

        elif cartela.B[2]==0 and cartela.I[2]==0 and cartela.N[2]==0 and cartela.G[2]==0 and cartela.O[2]==0:
            print("Bingo!! Na coluna [3]")
        
        elif cartela.G[0]==0 and cartela.G[1]==0 and cartela.G[2]==0 and cartela.G[3]==0 and cartela.G[4]==0:
            print("Bingo! Na linha [G]")

        elif cartela.B[3]==0 and cartela.I[3]==0 and cartela.N[3]==0 and cartela.G[3]==0 and cartela.O[3]==0:
            print("Bingo!! Na coluna [4]")

        elif cartela.O[0]==0 and cartela.O[1]==0 and cartela.O[2]==0 and cartela.O[3]==0 and cartela.O[4]==0:
            print("Bingo! Na linha [O]")
        
        elif cartela.B[4]==0 and cartela.I[4]==0 and cartela.G[4]==0 and cartela.O[4]==0:
            print("Bingo!! Na coluna [5]")

        elif cartela.B[0]==0 and cartela.I[1]==0 and cartela.N[2]==0 and cartela.G[3]==0 and cartela.O[4]==0:
            print("Bingo! Na diagonal!")

        elif cartela.O[0]==0 and cartela.G[1]==0 and cartela.N[2]==0 and cartela.I[3]==0 and cartela.O[4]==0:
            print("Bingo! Na diagonal!")
        

novoBingo = bingo()
novoBingo.tabela()
sorte=Bingo_Sorteio()
sorte.menu(novoBingo)