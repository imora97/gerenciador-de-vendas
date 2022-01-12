# classe principal
# import - importa funções, variáveis, classes de outros arquivos

# de /model/cliente.py importe Cliente (é uma classe)
from model.cliente import Cliente

# carrega o arquivo do diretório /model/cliente_dao.py
# e define um apelido chamado funcoes_clientes para prover 
# acesso as funções definidas no arquivo importado
import model.cliente_dao as funcoes_clientes

# ADCIONAR CLIENTES
for i in range(0, 5):
    novo_cliente = Cliente(None, f'Cliente-{i}', 'rua a', '75 9 8888888')
    # CHAMADA DA FUNÇÃO DE ADICIONAR UM CLIENTE EM CLIENTE_DAO.PY
    funcoes_clientes.adicionar(novo_cliente)

# EXCLUI CLIENTE

"""funcoes_clientes.excuir(0)
funcoes_clientes.excuir(10)
funcoes_clientes.excuir(5)
funcoes_clientes.excuir(7)
funcoes_clientes.excuir(11)
funcoes_clientes.excuir(14)
funcoes_clientes.excuir(13)
funcoes_clientes.excuir(12)"""

# EDIÇÃO DE UM CLIENTE

# 1 - Qual o ID do cliente que desejo editar?
#id_cliente = 4

# 2 - Pegar todas as informações do cliente com ID = 4 
# (Pegar o objeto cliente na lista de clientes que possui o ID 4)

#cliente_edit = funcoes_clientes.pegarCliente(id_cliente) # retorna o objeto cliente com id = 4

# 3 - Fazer a edição dos campos localmente
"""cliente_edit.nome = 'Kauãn Nascimento'
cliente_edit.endereco = 'Rua Alguma coisa, n 789'
cliente_edit.telefone = '75 9 7894-2310'"""

# 4 - salvar o elemento na lista
"""funcoes_clientes.editar(cliente_edit)"""

# imprimir todos os clientes
funcoes_clientes.listar_todos()
