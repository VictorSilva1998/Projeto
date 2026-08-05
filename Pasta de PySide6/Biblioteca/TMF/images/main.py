from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import QApplication, QCheckBox, QFrame, QHBoxLayout, QLabel, QLineEdit, QMessageBox, QTabWidget, QVBoxLayout, QWidget
import sys
CADASTRO, LOGIN, CONTA, OPERACOES = 0, 1, 2, 3

def _aba (widget):
    layout = QVBoxLayout (widget)
    layout.setContentsMargins (60, 44, 60, 44)
    layout.setSpacing (10)
    return layout

class AbaCadastro (QWidget):
    def __init__ (self, janela):
        super().__init__()
        self.janela = janela
        layout = _aba (self)

        self.nome = campo

def main ():
    app = QApplication (sys.argv)
    app.setApplicationName ("TMF")
    app.setFont (QFont ("Segoe UI", 10))