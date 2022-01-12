from qt_core import *
import model.cliente_dao as cliente_dao
import model.peca_dao as peca_dao

FILE_UI = 'view/cad_venda.ui'


class CadVenda(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)

        # listas
        self.lista_clientes = None
        self.lista_pecas = None

        self.lista_itens = None

        # cliente atual
        self.cliente_atual = None
        self.peca_atual = None

        # evento do botão finalizar
        self.finalizar_btn.clicked.connect(self.finalizar_venda)

        # adicionar peça
        self.add_peca_btn.clicked.connect(self.add_item_lista)

        self.carrega_clientes()
        self.carrega_pecas()

    def add_item_lista(self):
        if self.quantidade.text() == '' or self.valor_unitario.text() == '':
            print('Insira os dados obrigatórios')
        else:
            #cria um novo item
            item = {'quantidade': self.quantidade.text(),
                    'peca': self.peca_atual}
            # adicionar na lista de itens
            self.lista_itens.append(item)

            self.atualiza_dados_venda()
    
    # atualizar os dados da venda (Qtd de itens e Total )
    def atualiza_dados_venda(self):
        #atualiza a quantidade de itens
        # mostra o tamanho da lista de itens

        #atualiza o total pago
        # varrer a lista de itens e somar todos os valores da multiplicação entre a 
        # quandidade de itens x o valor da peça


    def carrega_clientes(self):
        # lista de clientes
        self.lista_clientes = cliente_dao.lista_clientes
        temp_lista = []  # armazenar os nomes dos clientes
        for c in self.lista_clientes:
            temp_lista.append(c.nome)
        # lista de nomes dos clientes
        self.clientes_comboBox.addItems(temp_lista)
        # evento que pega o INDEX do cliente selecionado
        self.clientes_comboBox.currentIndexChanged.connect(self.pega_cliente)

    def carrega_pecas(self):
        # lista de peças
        self.lista_pecas = peca_dao.lista_pecas
        for p in self.lista_pecas:
            self.pecas_listWidget.addItem(p.nome)

        self.pecas_listWidget.currentRowChanged.connect(self.pega_peca)

    def pega_peca(self, index):
        self.peca_atual = self.lista_pecas[index]
        self.valor_unitario.setText(str(self.peca_atual.valor))

    def pega_cliente(self, index):
        self.cliente_atual = self.lista_clientes[index]
        self.label_id.setText(f'# {self.cliente_atual.id}')

    def finalizar_venda(self):
        print(f"Cliente:{self.cliente_atual.nome}")
