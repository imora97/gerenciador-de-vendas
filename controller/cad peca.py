from model.peca import Peca
import model.peca_dao as pecas_dao
from qt_core import *

FILE_UI = 'view/cad_peca.ui'


class CadPecaWindow(QWidget):
    def __init__(self, janela_peca):
        super().__init__()
        uic.loadUi(FILE_UI, self)

        self.janela_peca = janela_peca

        # eventos dos botões
        self.cancelar_btn.clicked.connect(self.fechar_janela)
        self.salvar_btn.clicked.connect(self.salvar)

    def fechar_janela(self):
        self.close()  # close - fechar

    def salvar(self):
        # pega os dados
        nome = self.nome.text()
        validade = self.validade.value()
        valor = self.valor.text()

        # cria o objeto
        nova_peca = Peca(None, nome, valor, validade)
        pecas_dao.adicionar(nova_peca)

        # atualiza tabela
        self.janela_peca.carrega_dados()

        # fecha janela
        self.close()
