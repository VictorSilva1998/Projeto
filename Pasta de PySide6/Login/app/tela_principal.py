from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout, QWidget

from app import IMAGEM_PERFIL
from app.usuario import Usuario

LARGURA = 520
ALTURA = 620
LARGURA_FOTO = 380

class PainelImagem (QLabel):
    def __init__ (self, caminho_imagem = IMAGEM_PERFIL, parent: QWidget | None = None):
        super ().__init__(parent)
        self.setObjectName ("Imagem")
        self.setAlignment (Qt.AlignCenter)
        self._carregar (caminho_imagem)

    def _carregar (self, caminho) -> None:
        pixmap = QPixmap (str (caminho))

        if pixmap.isNull ():
            self.setText (f"Imagem não encontrada: \n{caminho.name}")
            return
        
        self.setPixmap (pixmap.scaled (LARGURA // 5, ALTURA, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation))

class Perfil (QFrame):
    def __init__ (self, parent: QWidget | None = None):
        super ().__init__ (parent)
        self.setObjectName ("Perfil")
        self._montar_interface ()

    def _montar_interface (self) -> None:
        layout = QVBoxLayout (self)
        layout.setContentsMargins (50, 50, 50, 50)
        layout.setSpacing (10)

class TelaPrincipal (QWidget):
    def __init__(self, usuario: Usuario | None = None):
        super ().__init__()

        self.setObjectName ("Tela Janela")
        self.setWindowTitle ("Tela Principal")
        self.setMinimumSize (LARGURA, ALTURA)

        self.painel_imagem = PainelImagem()

        layout = QVBoxLayout (self)
        layout.setContentsMargins (30, 30, 30, 30)
        layout.setSpacing (0)
        layout.addWidget (self.painel_imagem, 1)

        texto_dados = (
            "<b>Victor Alexandre da Silva</b><br>"
            "Celular: (21) 99514-3912<br>"
            "E-mail: victor.alexandre9813@gmail.com"
        )
        self.label_dados = QLabel(texto_dados)
        self.label_dados.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.painel_imagem)
        layout.addWidget(self.label_dados)

        self.setLayout(layout)