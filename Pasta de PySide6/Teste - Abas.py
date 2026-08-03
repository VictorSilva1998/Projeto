import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QLabel, QVBoxLayout

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemplo de Abas com PySide6")
        self.resize(400, 300)

        # Criar o widget de abas
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Aba 1
        self.aba1 = QWidget()
        layout1 = QVBoxLayout()
        layout1.addWidget(QLabel("Conteúdo da Primeira Aba"))
        self.aba1.setLayout(layout1)
        self.tabs.addTab(self.aba1, "Aba 1")

        # Aba 2
        self.aba2 = QWidget()
        layout2 = QVBoxLayout()
        layout2.addWidget(QLabel("Conteúdo da Segunda Aba"))
        self.aba2.setLayout(layout2)
        self.tabs.addTab(self.aba2, "Aba 2")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = JanelaPrincipal()
    janela.show()
    sys.exit(app.exec())
