# importa todas as bibliotecas definidas 
# no arquivo qt_core.py
from qt_core import *
#importa a classe MainWindow - Janela principal
from controller.main_window import MainWindow

import model.cliente_dao as funcoes_clientes
import model.peca_dao as peda_dao
from model.cliente import Cliente
from model.peca import Peca

os.environ['XDG_SESSION_TYPE'] = 'Wayland' # APENAS PARA O LINUX

def carrega_dados():
    # ADCIONAR CLIENTES
    for i in range(0, 15):
        novo_cliente = Cliente(None, f'Cliente-{i}', 'rua alguma coisa', '75 9 8888888')
        # CHAMADA DA FUNÇÃO DE ADICIONAR UM CLIENTE EM CLIENTE_DAO.PY
        funcoes_clientes.adicionar(novo_cliente)
        peda_dao.adicionar(Peca(None, 'Peca '+str(i), 50+i, 2*i))

    # add peças

# cria a aplicação
app = QApplication(sys.argv)
carrega_dados()
# definir os widgets que aparecerão na tela
window = MainWindow()
window.show() # carregar o elemento para a tela
app.setStyle('Fusion')
#executar o aplicativo
app.exec()
