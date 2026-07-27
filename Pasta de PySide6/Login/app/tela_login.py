from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QCheckBox, QFrame, QHBoxLayout, QLabel, QLineEdit, QMessageBox, QVBoxLayout, QWidget, QPushButton
from app import IMAGEM_LOGIN
# AUTENTICATOR
# USUÁRIO

LARGURA = 760
ALTURA = 420

class PainelImagem (QLabel):
    def __init__ (self, caminho_imagem = IMAGEM_LOGIN, parent: QWidget | None = None):
        super ().__init__ (parent)
        self.setObjectName ("Imagem")
        self.setAlignment (Qt.AlignCenter)
        self._carregar (caminho_imagem)
    
    def _carregar (self, caminho) -> None:
        pixmap = QPixmap (str (caminho))
        if pixmap.isNull():
            self.setText (f"Imagem não encontrada: \n {caminho.name}")
            return
        self.setPixmap (pixmap.scaled (LARGURA // 2, ALTURA, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation))

class FormularioLogin (QFrame):
    login_solicitado = Signal (str, str)
    senha_esquecida = Signal ()

    def __init__(self, parent : QWidget | None = None):
        super().__init__(parent)
        self.setObjectName ("Formulario")
        self._montar_interface ()
    
    def _montar_interface (self) -> None:
        layout = QVBoxLayout (self)
        layout.setContentsMargins (40, 40, 40, 40)
        layout.setSpacing (10)

        titulo = QLabel ("Bem Vindo!")
        titulo.setObjectName ("Titulo")

        subtitulo = QLabel ("Entre com sua conta para continuar")
        subtitulo.setObjectName ("Subtitulo")

        self.campo_usuario = QLineEdit ()
        self.campo_usuario.setPlaceholderText ("Usuário")

        self.campo_senha = QLineEdit ()
        self.campo_senha.setPlaceholderText ("Senha")
        self.campo_senha.setEchoMode (QLineEdit.Password)

        self.mostra_senha = QCheckBox ("Mostrar Senha")
        self.mostra_senha.toggle.connect (self._alterar_senha)

        self.botao_entrar = QPushButton ("Entrar")
        self.botao_entrar.setObjectName ("Botão Entrar")
        self.botao_entrar.setCursor (Qt.PointingHandCursor)
        self.botao_entrar.clicked.connect (self._emitir_login)

    def _alterar_senha (self, marcado: bool) -> None:
        self.campo_senha.setEchoMode (QLineEdit.Normal if marcado else QLineEdit.Password)

    def _emitir_login (self) -> None:
        self.login_solicitado.emit (self.campo_usuario.text (), self.campo_senha ())