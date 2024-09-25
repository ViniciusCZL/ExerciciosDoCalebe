class Livros:
    def __init__(self,titulo,autor):
        self.titulo=titulo
        self.autor=autor
        self.emprestado=False

    def __str__(self):
        return f"{self.titulo} {self.autor}"
    