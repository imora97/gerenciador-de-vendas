# Lista para armazenar as peças


lista_pecas = []


def adicionar(nova_peca):
    novo_id = len(lista_pecas)
    nova_peca.id = novo_id
    lista_pecas.append(nova_peca)


def pegarPeca(id):
    for peca in lista_pecas:
        if peca.id == id:
            return peca
    return None


def editar(peca):
    for i in range(0, len(lista_pecas)):
        if peca.id == lista_pecas[i].id:
            lista_pecas[i] = peca


def excluir(id):
    for peca in lista_pecas:
        if peca.id == id:
            lista_pecas.remove(peca)
