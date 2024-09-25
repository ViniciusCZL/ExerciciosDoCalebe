class Livro():
    def __init__(self,nome,autor,editora,paginas) -> None:
        self.nome=nome
        self.autor=autor
        self.editora=editora
        self.paginas=paginas

    def alterareditora(self):
        print(self.editora)
        editareditora=input("Digite a nova editora: ")
        self.editora=editareditora

    def ListarPaginas(self):
        print(self.paginas)

livro=Livro("Vinícius por Vinícius os dois lados de mim","Vinícius","Saraiva",695)

def mostrarMenu():
    print("_______MENU_______")
    print("[1]Alterar Editora")
    print("[2]Listar  Paginas")



while True:
    mostrarMenu()
    op=int(input("Digite uma opção: "))

    if op==1:
        livro.alterareditora()

    elif op==2:
        livro.ListarPaginas()

    else:
        break
