class Autor:
    def __init__(self, nome, nacionalidade):
        self._nome = nome
        self._nacionalidade = nacionalidade

    def get_nome(self):
        return self._nome

    def get_nacionalidade(self):
        return self._nacionalidade


class Livro:
    def __init__(self, titulo, autor, isbn):
        self._titulo = titulo
        self._autor = autor
        self._isbn = isbn
        self._disponivel = True

    def adicionar(self, biblioteca):
        biblioteca.adicionar_livro(self)
