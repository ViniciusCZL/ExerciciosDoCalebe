from personagem import Cavaleiro
from arma import Espada
from javali import Javali
from Peitoral import Armadura
import random

class jogo:
    def personagem(self):
        if DarkWarrior.vida<=0:
            print("Se Fodeu!")
            print("Game Over!!!")
    def atacar(self):
        ataqueBase=DarkWarrior.força + ArmaEspada.DanoBase
        critico = random.uniform(0,1.0)
        
        if Alvo.vida>0:
            if critico<=0.1:
                Ataque=ataqueBase*2
                defesa=Alvo.defesa/100
                Ataque=Ataque-defesa
                Alvo.vida-=Ataque
                print("ataque crítico, você acertou", Ataque,"de Dano no inimigo, inimigo", Alvo.nome,"ficou com", Alvo.vida,"de HP")

            elif critico>0.1:
                defesa=Alvo.defesa/100
                Ataque=ataqueBase-defesa
                Alvo.vida-=Ataque
                print("ataque, você acertou", Ataque,"de Dano no inimigo, inimigo", Alvo.nome,"ficou com", Alvo.vida,"de HP")

        elif Alvo.vida<=0:
            print("Inimigo Javali Vermelho morreu!")  
            print("Você ganhou!")
        
    def inimigoAtaque(self):
        self.ataqueBase=Alvo.força + Alvo.resistencia
        self.defesa=DarkWarrior.defesa + chestplate.Defesa /100
        DarkWarrior.vida=DarkWarrior.vida+self.defesa-self.ataqueBase
        chestplate.Durabilidade= self.ataqueBase-self.defesa-chestplate.Durabilidade
        print("Voce sofreu", self.ataqueBase, "de dano do", Alvo.nome, "você ficou com", DarkWarrior.vida,"de HP.")   

    def cura(self):
        if DarkWarrior.vida>500:
            DarkWarrior.vida=500
            print("ja está com vida máxima.")
        
        else:
            DarkWarrior.vida+=100
            if DarkWarrior.vida>500:
                DarkWarrior.vida=500

            print("Você usou Bálsamo de Cura Médio, restaurando 100 de HP, do", DarkWarrior.nome,"ponto de vida atual",DarkWarrior.vida)

    def menuJogo(self):
        while True:
            print("[1] Atacar")
            print("[2] Fugir")
            print("[3] Usar Item")
            op=int(input("Digite a ação que deseja fazer."))

            if op==1:
                jogar.atacar()
                jogar.inimigoAtaque()

            elif op == 2:
                print("o",DarkWarrior.nome ,"fugiu")

            elif op == 3:
                jogar.cura()

        

DarkWarrior=Cavaleiro(500,10,12,4, Espada,Armadura)
ArmaEspada=Espada()
chestplate=Armadura("Cota de Malha",20,1000)
Alvo=Javali("Javali Vermelho", 200, 14, 13, 8, 10)
jogar = jogo()

jogar.menuJogo()
