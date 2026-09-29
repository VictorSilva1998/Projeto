from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QPushButton
)

candidatos = [
    ("01", "Evelyn Palbueno"),
    ("02", "Mauricio de Souza"),
    ("03", "Ederson da Costa"),
]

class TelaZeresima(QDialog):

    zeresima_emitida = Signal()

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Relatório Inicial (Zerésima)")
        self.resize(500, 400)

        self.setModal(True)

        layout = QVBoxLayout()

        texto = "RELATÓRIO INICIAL (ZERÉSIMA)\n\n"

        for numero, nome in candidatos:
            texto += f"{numero} - {nome}: 0 votos\n"

        texto += "\nBrancos: 0 votos"
        texto += "\nNulos: 0 votos"
        texto += "\n\nTOTAL: 0 votos"

        relatorio = QLabel(texto)
        layout.addWidget(relatorio)

        botao_confirmar = QPushButton("Confirmar Zerésima")
        botao_confirmar.clicked.connect(self.confirmar_zeresima)

        layout.addWidget(botao_confirmar)

        self.setLayout(layout)

    def confirmar_zeresima(self):
        self.zeresima_emitida.emit()
        self.close()