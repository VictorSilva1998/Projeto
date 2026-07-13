from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
from PySide6.QtCore import Qt
import sys

class HelloWorldWindow (QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuração básica da tela
        self.setWindowTitle ("Hello World App")
        self.setGeometry (100, 100, 400, 200)
        # Criamos um texto e uma label
        label = QLabel ("Hello World", self)
        label.setGeometry (150, 80, 200, 30)
        # Estilo do Texto
        label.setStyleSheet ("font-size: 23px; font-weight: bold")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

if __name__ == "__main__":
    app = QApplication (sys.argv)
    window = HelloWorldWindow ()
    window.show ()
    sys.exit (app.exec ())