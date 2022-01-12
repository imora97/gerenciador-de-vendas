from controller.cad_peca import CadPecaWindow
import model.peca_dao as peca_dao
from qt_core import *

FILE_UI = 'view/pecas.ui'


class PecaPage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)

        self.peca_window = None
        self.carrega_dados()

        # evento do botão nova peça
        self.novo_btn.clicked.connect(self.nova_peca)

        #configurações da tabela
        self.tabela.verticalHeader().setVisible(False)
        self.tabela.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents) # ajusta ao conteúdo da célula
        self.tabela.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch) # ajusta pelo à lagura da tela

    def nova_peca(self):
        # criação da janela de cadastro
        self.peca_window = CadPecaWindow(self)
        self.peca_window.show()
    
    def carrega_dados(self):
        lista = peca_dao.lista_pecas
        self.tabela.setRowCount(0)
        for p in lista:
            self.add_linha(p)
    
    def add_linha(self, p):
        rowCount = self.tabela.rowCount()
        self.tabela.insertRow(rowCount)

        id = QTableWidgetItem(str(p.id))
        nome = QTableWidgetItem(p.nome)
        valor = QTableWidgetItem(str(p.valor))
        validade = QTableWidgetItem(str(p.validade))

        #insere os elementos na tabela na coluna correspondente
        # (linha, coluna, item)
        self.tabela.setItem(rowCount, 0, id)
        self.tabela.setItem(rowCount, 1, nome)
        self.tabela.setItem(rowCount, 2, valor)
        self.tabela.setItem(rowCount, 3, validade)
