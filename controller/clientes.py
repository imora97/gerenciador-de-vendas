from qt_core import *
from controller.cad_cliente import CadClienteWindow
import model.cliente_dao as funcoes_clientes

FILE_UI = 'view/clientes.ui'

class ClientesPage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)
        
        self.cliente_window = None

        #carrega dados da lista de clientes
        self.carrega_dados()

        # evento do botão nova peça
        self.novo_btn.clicked.connect(self.novo_cliente)

        #configurações da tabela
        self.tabela.verticalHeader().setVisible(False)
        self.tabela.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) #ajusta ao tamanho da tela
        self.tabela.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents) # ajusta pelo conteúdo da coluna
        self.tabela.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents) # ajusta pelo conteúdo da coluna
        self.tabela.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents) # ajusta pelo conteúdo da coluna

    def novo_cliente(self):
        # criação da janela de cadastro
        self.cliente_window = CadClienteWindow(self)
        self.cliente_window.show()
    
    #carrega os dados na minha tabela
    def carrega_dados(self):
        # pegar a lista de todos os clientes
        lista_clientes = funcoes_clientes.lista_clientes
        # zera a tabela - ir para a linha zero da tabela
        self.tabela.setRowCount(0)
        # adcionar os elementos na tabela
        for cliente in lista_clientes:
            self.add_linha(cliente)
    
    def add_linha(self, cliente):
        rowCount = self.tabela.rowCount()
        self.tabela.insertRow(rowCount)

        # elementos de cada coluna da tabela
        # OBS.: SÓ ACEITA STRING - NUM PRECISAM SER CONVERTIDOS ATRAVÉS DA FUNÇÃO STR
        id = QTableWidgetItem(str(cliente.id))
        nome = QTableWidgetItem(cliente.nome)
        endereco = QTableWidgetItem(cliente.endereco)
        telefone = QTableWidgetItem(cliente.telefone)

        #insere os elementos na tabela na coluna correspondente
        # (linha, coluna, item)
        self.tabela.setItem(rowCount, 0, id)
        self.tabela.setItem(rowCount, 1, nome)
        self.tabela.setItem(rowCount, 2, endereco)
        self.tabela.setItem(rowCount, 3, telefone)

