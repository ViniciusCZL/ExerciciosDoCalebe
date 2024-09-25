print("[1] Médico")
print("[2] Paciente")
login=str(input("Digite aqui:"))

loginM_01="Vinicius"
senhaM_01="cruz"

loginM_02="professor"
senhaM_02="senha123"

consultas={}

while True:
    if login==1:
        loginM=input("Digite seu login: ")
        senhaM=input("Digite sua Senha: ")

        while True:
            if (loginM==loginM_01 and senhaM==senhaM_01) or (loginM==loginM_02 and senhaM==senhaM_02):
                print(f"Logado {loginM}")
                print("[1] Ver Consultas")
                mc=int(input("digite aqui: "))
                if mc==1:
                    print(consultas)
                    print("[1] Realizar consulta.")
                    
    elif login==2:
        loginP=