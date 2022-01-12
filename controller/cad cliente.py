from model.cliente import Cliente
import model.cliente_dao as funcoes_clientes
from qt_core import *

FILE_UI = 'view/cad_cliente.ui'


class CadClienteWindow(QWidget):
    def __init__(self, janela_cliente):
        super().__init__()
        uic.loadUi(FILE_UI, self)

        # uma forma de acessar os métodos da janela cliente (janela pai)
        self.janela_cliente = janela_cliente

        # eventos dos botões
        self.cancelar_btn.clicked.connect(self.fechar_janela)
        self.salvar_btn.clicked.connect(self.salvar)

    def fechar_janela(self):
        self.close()  # close - fechar

    def salvar(self):
        # pega os dados
        nome = self.nome.text()
        endereco = self.endereco.text()
        telefone = self.telefone.text()
        # cria o objeto
        novo_cliente = Cliente(None, nome, endereco, telefone)
        funcoes_clientes.adicionar(novo_cliente)
        # atualizar a tabela
        self.janela_cliente.carrega_dados()
        #fechar a janela
        self.close()
