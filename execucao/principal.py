from modelo.produto import Produto

# comentario de uma linha
''' comentario mais de uma linha '''

if __name__ == '__main__':
    # Saida de dados
    print('Seja Bem Vindos')

    # produto => Instancia
    # Produto => Objeto, construtor

    produto = Produto()

    # Entrada de dados
    produto.nome = 'Playstation 4'
    produto.preco = 2000.0
    produto.quantidade = 3
    produto.descricao = 'Sony'

    produto2 = Produto()
    produto2.nome = 'Xbosta one'
    produto2.preco = 1000.0
    produto2.quantidade = 3
    produto2.descricao = 'Microsoft'

    # Saida de dados
    print('Produto 1')
    print(produto.nome)
    print(produto.preco)
    print(produto.quantidade)
    print(produto.descricao)

    # Saida composicao de string
    print('Produto 2')
    print('Nome : %s' % produto2.nome)
    print('Preco : %f' % produto2.preco)
    print('Quantidade: %d' % produto2.quantidade)
    print('Descricao : %s' % produto2.descricao)

    # SAidade composicao de string
    print('%s, %f, %d, %s' % (produto.nome, produto.preco, produto.quantidade, produto.descricao))

    # String Format
    print('{}, {}, {}'.format(produto2.nome, produto2.preco, produto2.quantidade))

    pass
