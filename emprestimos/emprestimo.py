class Emprestimo:
    def __init__(self, pessoa, livro):
        self.pessoa = pessoa
        self.livro = livro
        self.ativo = True
        self.livro.disponivel = False

    def devolver(self):
        self.livro.disponivel = True
        self.ativo = False
