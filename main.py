# classe principal
# import - importa funções, variáveis, classes de outros arquivos

# de /model/cliente.py import Cliente (é uma classe)
from model.cliente import Cliente

# carrega o arquivo do diretório /model/cliente_dao.py
# e define um apelido chamado funcoes_clientes para prover
# acesso as funções definidas no arquivo importado
import model.cliente_DAO as funcoes_clientes

# adicionar vários clientes
for i in range(0,15):
    novo_cliente = Cliente(i, f'Cliente-{i}', 'rua a', '71 9 88888888')
    funcoes_clientes.append(novo_cliente)

funcoes_clientes.listar_todos()


