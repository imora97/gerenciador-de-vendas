from qt_core import *

FILE_UI = 'view/resumo.ui'

class ResumoPage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)
