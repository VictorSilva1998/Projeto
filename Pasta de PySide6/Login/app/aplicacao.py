import sys
from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication

from app.estilos import ESTILO, Cores
from app.tela_login import TelaLogin
from app.tela_principal import TelaPrincipal
from app.usuario import Usuario

class Aplicacao:
    def __init__(self):
        self._app = QApplication (sys.argv)
        self._configurar_tema()

        self.janela = TelaLogin()
        self.janela_principal: TelaPrincipal | None = None
        self.janela.autenticado.connect (self._abrir_tela_principal)

    def _configurar_tema (self) -> None:
        self._app.setStyle ("Fusion")
        self._app.setStyleSheet (ESTILO)

        paleta = self._app.palette()
        paleta.setColor(QPalette.PlaceholderText, QColor(Cores.PLACEHOLDER))
        self._app.setPalette (paleta)

    def _abrir_tela_principal (self, usuario: Usuario) -> None:
        self.janela_principal = TelaPrincipal (usuario)
        self.janela_principal.show ()
        self.janela.close ()

    def executar (self) -> int:
        self.janela.show()
        return self._app.exec()