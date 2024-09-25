from Biblioteca import biblioteca
from livros import Livros

def ExibirMenu():
    print("1. Adicionar Livro")
    print("2. Consultar detalhes do livro")
    print("3. Emprestar um livro")
    print("4. Listar todos os livros da biblioteca")
    print("5. Devolver livro")
    print("6. Sair")

Biblioteca=biblioteca()
while True:
    ExibirMenu()
    op = int(input("Digite a opção: "))
    if op == 1:
        titulo =input("Digite o titulo do livro: ")
        autor =input("Digite o autor do livro: ")
        livro=Livros(titulo,autor)
        Biblioteca.AdicionarLivro(livro)