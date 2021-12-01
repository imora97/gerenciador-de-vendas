# Padrão DAO (Data Access Object)
# Centraliza o acesso aos dados dos objetos 

# lista que irá armazenar todos os clientes da
lista_clientes = []

# adicionar novo cliente
def adicionar(novo_cliente):
    lista_clientes.append(novo_cliente)

# editar cliente
def editar():
    pass

# excluir cliente
def excluir():
    pass

# listar todos os clientes
def listar_todos():
    # passa por todos os clientes da lista e chama a função "imprime()" desses objetos
    for cliente in lista_clientes:
        cliente.imprime()

# pegar um cliente específico
def lista_clientes():
    pass


