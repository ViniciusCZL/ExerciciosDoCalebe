import random

class bingo:
    B=[]
    I=[]
    N=[]
    G=[]
    O=[]
    def tabela(self):
        while len(self.B) != 5:
            bnumero = random.randint(1,15)
            if not bnumero in self.B and len(self.B) != 6:
                self.B.append(bnumero)

        while len(self.I) != 5:
            Inumero=random.randint(16,30)
            if not Inumero in self.I and len(self.I) != 6:
                self.I.append(Inumero)

        while len(self.N) != 4:
            Nnumero=random.randint(31,45)
            if not Nnumero in self.N and len(self.N) != 6:
                self.N.append(Nnumero)

        while len(self.G) != 5:
            Gnumero=random.randint(46,60)
            if not Gnumero in self.G and len(self.G) != 6:
                self.G.append(Gnumero)

        while len(self.O) != 5:
            Onumero=random.randint(61,75)
            if not Onumero in self.O and len(self.O) != 5:
                self.O.append(Onumero)

        for i in range(1):
            print(self.B)
            print(self.I)
            print(self.N)
            print(self.G)
            print(self.O)


                