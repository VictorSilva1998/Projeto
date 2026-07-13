from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
import sys

class HelloWorldWindow (QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuração básica da tela
        self.setWindowTitle ("Hello World App")
        self.setGeometry (150, 50, 600, 700)
        # Criamos um texto e uma label
        label = QLabel ("Victor Alexandre da Silva", self)
        label.setGeometry (100, 80, 400, 100)
        # Estilo do Texto
        label.setStyleSheet ("font-size: 23px; font-weight: bold")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Adicionando uma imagem
        label2 = QLabel (self)
        label2.setGeometry (150, 150, 500, 500)
        pixmap = QPixmap ("HelloWorld.png")
        label2.setPixmap (pixmap.scaled (300, 300))
        # Cria um botão
        self.botao = QPushButton("Botão", self)
        self.botao.setGeometry (250, 600, 60, 40)
        self.botao.clicked.connect(self.click)

    def click (self):
        print("Você clicou no Botão! Parabéns!!!!!")

if __name__ == "__main__":
    app = QApplication (sys.argv)
    window = HelloWorldWindow ()
    window.show ()
    sys.exit (app.exec ())