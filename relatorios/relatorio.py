class Relatorio:
    def listar_emprestimos(self, emprestimos):
        if not emprestimos:
            return "Nenhum empréstimo foi realizado."

        linhas = ["===== EMPRÉSTIMOS ====="]
        for emprestimo in emprestimos:
            situacao = "Ativo" if emprestimo.ativo else "Devolvido"
            linhas.append(
                f"{emprestimo.livro.titulo} | "
                f"{emprestimo.pessoa.nome} | {situacao}"
            )
        return "\n".join(linhas)
