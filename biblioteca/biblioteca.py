from emprestimos.emprestimo import Emprestimo


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.pessoas = []
        self.emprestimos = []

    def adicionar_livro(self, livro):
        if self.buscar_livro(livro.codigo) is not None:
            return False
        self.livros.append(livro)
        return True

    def adicionar_pessoa(self, pessoa):
        if self.buscar_pessoa(pessoa.matricula) is not None:
            return False
        self.pessoas.append(pessoa)
        return True

    def buscar_livro(self, codigo):
        for livro in self.livros:
            if livro.codigo == codigo:
                return livro
        return None

    def buscar_pessoa(self, matricula):
        for pessoa in self.pessoas:
            if pessoa.matricula == matricula:
                return pessoa
        return None

    def fazer_emprestimo(self, codigo, matricula):
        livro = self.buscar_livro(codigo)
        pessoa = self.buscar_pessoa(matricula)

        if livro is None or pessoa is None or not livro.disponivel:
            return False

        self.emprestimos.append(Emprestimo(pessoa, livro))
        return True

    def devolver_livro(self, codigo):
        for emprestimo in self.emprestimos:
            if emprestimo.livro.codigo == codigo and emprestimo.ativo:
                emprestimo.devolver()
                return True
        return False

    def proximo_codigo(self):
        if not self.livros:
            return 1
        return max(livro.codigo for livro in self.livros) + 1
