# Descrição: Classe Cliente
# Contém os atributos do cliente

class Cliente():
    def __init__(self, id, nome, endereco, telefone):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
    
    #função da minha classe
    def print(self):
        print(self.id, self.nome, self.endereco, self.telefone)
