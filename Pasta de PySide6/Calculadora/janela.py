import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget
)
from soma import Soma
from subtracao import Subtracao
from multiplicacao import Multiplicacao
from divisao import Divisao

OPERACOES = {
    "+": Soma,
    "-": Subtracao,
    "x": Multiplicacao,
    "/": Divisao
}

ESTILO = """
QWidget {
    background-color: #f2f2f2;
    font-family: Segoe UI, Arial;
}
QLabel#visor {
    background-color: #ffffff;
    border: 1px solid #cccccc;
    color: #222222;
    font-size: 28px;
    padding: 12px;
}
QLabel#conta {
    color: #777777;
    font-size: 13px;
    padding-left: 4px;
}
QPushButton {
    background-color: #ffffff;
    border: 1px solid #cccccc;
    color: #222222;
    font-size: 18px;
    min-width: 56px;
    min-height: 48px;
}
QPushButton:hover {
    background-color: #e8e8e8;
}
QPushButton:pressed {
    background-color: #dcdcdc;
}
"""

class Calculadora(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")

        self.digitado = "0"
        self.a = None
        self.classe = None
        self.zerar = False

        self.conta = QLabel("")
        self.conta.setObjectName("conta")
        self.conta.setAlignment(Qt.AlignRight)

        self.visor = QLabel(self.digitado)
        self.visor.setObjectName("visor")
        self.visor.setAlignment(Qt.AlignRight)
        grade = QGridLayout()
        botoes = [
            ("c", 0, 0), ("<", 0, 1), ("+/-", 0, 2), ("/", 0, 3),
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("x", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("+", 3, 3),
            ("0", 4, 0), (",", 4, 1), ("=", 4, 2), 
        ]

        for texto, linha, coluna in botoes:
            botao = QPushButton(texto)
            largura = 2 if texto == "=" else 1
            botao.clicked.connect(self.criar_acao(texto))
            grade.addWidget(botao, linha, coluna, 1, largura)
        
        layout = QVBoxLayout()
        layout.addWidget(self.conta)
        layout.addWidget(self.visor)
        layout.addLayout(grade)
        self.setLayout(layout)

    def criar_acao(self, texto):
        return lambda checked=False: self.clicar(texto)
    
    def clicar(self, texto):
        if texto.isdigit():
            self.digitar(texto)

        elif texto in OPERACOES:
            self.escolher_operacao(texto)

        elif texto == "=":
            self.calcular()

        elif texto == "c":
            self.limpar()

        elif texto == "<":
            self.apagar()

        elif texto == "+/-":
            self.inverter_sinal()

        elif texto == ",":
            if "," not in self.digitado:
                self.mostrar(self.digitado + ",")

    def digitar(self, tecla):
        if self.zerar:
            self.mostrar(tecla)
            self.zerar = False

        elif self.digitado == "0":
            self.mostrar(tecla)

        else:
            self.mostrar(self.digitado + tecla)

    def valor_do_visor(self):
        return float(self.digitado.replace(",", "."))

    def mostrar(self, numero):
        if isinstance(numero, float) and numero.is_integer():
            numero = int(numero)

        self.digitado = str(numero).replace(".", ",")
        self.visor.setText(self.digitado)
    
    def escolher_operacao(self, simbolo):
        if self.classe is not None and not self.zerar:
            b = self.valor_do_visor()

            try:
                operacao = self.classe(self.a, b)
                self.a = operacao.calcular()
            except ZeroDivisionError:
                self.visor.setText("Erro")
                self.conta.setText("Divisão por zero")
                self.classe = None
                self.a = None
                return

            self.mostrar(self.a)

        else:
            self.a = self.valor_do_visor()

        self.classe = OPERACOES[simbolo]
        self.conta.setText(f"{self.a:g} {simbolo}")
        self.zerar = True

    def calcular(self):
        if self.classe is None:
            return

        b = self.valor_do_visor()

        operacao = self.classe(self.a, b)

        try:
            resultado = operacao.calcular()

        except ZeroDivisionError:
            self.visor.setText("Erro")
            self.conta.setText("Divisão por zero")
            self.a = None
            self.classe = None
            self.zerar = True
            return

        expressao = f"{self.a:g} {operacao.simbolo} {b:g} ="

        self.conta.setText(expressao)
        self.mostrar(resultado)

        self.a = resultado
        self.classe = None
        self.zerar = True

    def limpar(self):
        self.digitado = "0"
        self.a = None
        self.classe = None
        self.zerar = False

        self.visor.setText("0")
        self.conta.clear()

    def apagar(self):
        if len(self.digitado) > 1:
            self.mostrar(self.digitado[:-1])
        else:
            self.mostrar("0")

    def inverter_sinal(self):
        valor = self.valor_do_visor()
        self.mostrar(str(valor * -1).replace(".", ","))

def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(ESTILO)
    janela = Calculadora()
    janela.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()