class Autor:
    def __init__(self, nome, nacionalidade):
        self.__nome = nome
        self.__nacionalidade = nacionalidade

    @property
    def nome(self):
        return self.__nome

    @property
    def nacionalidade(self):
        return self.__nacionalidade

class Livro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__disponivel = True

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor

    @property
    def isbn(self):
        return self.__isbn

    @property
    def disponivel(self):
        return self.__disponivel

    @disponivel.setter
    def disponivel(self, status):
        self.__disponivel = status

    def adicionar(self, biblioteca):
        biblioteca.adicionar_livro(self)

    def buscar(self, biblioteca, titulo=None, nome_autor=None):
        return biblioteca.buscar_livro(titulo, nome_autor)

    def emprestar(self, usuario):
        if self.__disponivel:
            usuario.emprestar_livro(self)
            self.__disponivel = False
        else:
            print("Livro indisponível.")

    def devolver(self, usuario):
        if self in usuario.livros_emprestados:
            usuario.devolver_livro(self)
            self.__disponivel = True
        else:
            print("Este livro não foi emprestado para este usuário.")

class Usuario:
    def __init__(self, nome, id):
        self.__nome = nome
        self.__id = id
        self.__livros_emprestados = []

    @property
    def nome(self):
        return self.__nome

    @property
    def id(self):
        return self.__id

    @property
    def livros_emprestados(self):
        return self.__livros_emprestados

    def emprestar_livro(self, livro):
        self.__livros_emprestados.append(livro)
        print(f"{livro.titulo} emprestado com sucesso para {self.__nome}.")

    def devolver_livro(self, livro):
        self.__livros_emprestados.remove(livro)
        print(f"{livro.titulo} devolvido com sucesso por {self.__nome}.")

class Biblioteca:
    def __init__(self):
        self.__livros = []

    @property
    def livros(self):
        return self.__livros

    def adicionar_livro(self, livro):
        self.__livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado à biblioteca.")

    def buscar_livro(self, titulo=None, nome_autor=None):
        resultado = []
        for livro in self.__livros:
            if titulo and titulo.lower() in livro.titulo.lower():
                resultado.append(livro)
            elif nome_autor and nome_autor.lower() in livro.autor.nome.lower():
                resultado.append(livro)
        return resultado

if __name__ == "__main__":
    autor1 = Autor("George Orwell", "Inglaterra")
    livro1 = Livro("1984", autor1, "123456789")
    usuario1 = Usuario("João", 1)

    biblioteca = Biblioteca()

    livro1.adicionar(biblioteca)
    livros_encontrados = livro1.buscar(biblioteca, titulo="1984")
    print(f"Livros encontrados: {[livro.titulo for livro in livros_encontrados]}")

    livro1.emprestar(usuario1)
    livro1.devolver(usuario1)
