tarefas=[]
l={}
def adicionarTarefa():
    z={}
    T=input("Digite a Tarefa que deseja adicionar a lista: ")
    z["Nome"] = T
    z["Status"]="Não Concluída"    
    tarefas.append(z)
def removerTarefa(R):
    tarefas.remove(R)
def visualizarLista():
    for i in tarefas:
        print(i["Nome"],i["Status"])
def tarefaConcluída(C):
    l["Tarefa"]=input("Digite a Tarefa: ")    
    l["Status"]=("Tarefa Concluída")
    tarefas.append(tarefas)
def mostrarmenu():
    print("##### MENU #####")
    print("[1] Adicionar Tarefa")
    print("[2] Visualizar Lista de Tarefas")
    print("[3] Remover Tarefa")
    print("[4] Tarefa Concluída")
    print("[5] Sair")
while True:
    mostrarmenu()
    op=int(input("Digite a opção que deseja:"))
    if op==1:
        
        adicionarTarefa()
    if op==2:
        visualizarLista()
    if op==3:
        visualizarLista()
        R=input("Digite a Tarefa que deseja remover da lista: ")
        removerTarefa(R)
    if op==4:
        visualizarLista()
        C=input("digite a tarefa que foi conluída: ")
        tarefaConcluída(C)
    if op==5:
        print("FINALIZADO")
        break
