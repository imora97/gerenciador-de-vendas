# Padrão DAO (Data Access Object)
# Centraliza o acesso aos dados dos objetos cliente

# lista que irá armazenar todos os clientes do sistema
lista_clientes = []

# Adcionar novo cliente
def adicionar(novo_cliente):
    # inserir o ID do cliente
    novo_id = len(lista_clientes)
    novo_cliente.id =  novo_id
    #insere o cliente na lista
    lista_clientes.append(novo_cliente)

# Retorna o cliente com o id informado


def pegarCliente(id):
    # busca na lista de clientes
    for cliente in lista_clientes:
        if cliente.id == id:  # verifica se o id do objeto na lista é igual ao enviado por parâmetro
            # retorna o objeto cliente
            return cliente  # return -> retornar

    # quando não encontrar nenhum cliente com o id informado
    return None  # None -> vazio

# Editar cliente - Dado um objeto cliente, buscar na
# lista através do seu ID e atualizá-lo


def editar(cliente):
    # achar a posição na lista em que o cliente a ser editado está armazenado
    for index in range(0, len(lista_clientes)):
        # pego o elemento com posição definido pelo index na lista
        cliente_atual = lista_clientes[index]
        if cliente.id == cliente_atual.id:
            # se forem iguais significa que o cliente está armazenado
            # na posição definida pelo index
            # substitui (atribui) o objeto da posição informada pelo index
            lista_clientes[index] = cliente

# Excluir cliente - Dado o ID do cliente, removê-lo da lista


def excuir(id_cliente):
    for index in range(0, len(lista_clientes)):
        cliente_atual = lista_clientes[index]
        if id_cliente == cliente_atual.id:
            del lista_clientes[index]
            # parar de buscar na lista, porque o id é único
            return  # retorna algo vazio apenas para quebrar o loop do for

# Listar todos os cliente


def listar_todos():
    # passa por todos os clientes da lista e
    # chama a função imprime() desses objetos
    for cliente in lista_clientes:
        cliente.imprime()

# Listar um cliente específico
# Dado o ID do cliente, imprimir seus dados


def lista_cliente(id):
    pass
