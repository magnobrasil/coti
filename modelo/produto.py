class Produto(object):
    # Atributos -> Variaveis globais da classe, caracteristicas.

    __nome = None
    __preco = None
    __quantidade = None
    __descricao = None

    # Construtor , cheio - > Parâmetros
    # Construtor com parametros opcionais

    def __init__(self, nome=None, preco=None, quantidade=None, descricao=None):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade
        self.__descricao = descricao

        pass

        # SETTERS - ENTRADA

    def set_nome(self, value):
        self.__nome = value

    def set_preco(self, value):
        self.__preco = value

    def set_quantidade(self, value):
        self.__quantidade = value

    def set_descricao(self, value):
        self.__descricao = value

        # GETTERS - SAIDA

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def get_quantidade(self):
        return self.__quantidade

    def get_descricao(self):
        return self.__descricao

    def __str__(self):
        return '{}, {}, {}, {}'.format(self.__nome, self.__preco, self.__quantidade, self.__descricao)

    pass
