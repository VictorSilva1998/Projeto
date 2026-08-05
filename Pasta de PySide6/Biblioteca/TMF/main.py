from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import QApplication, QCheckBox, QFrame, QHBoxLayout, QLabel, QLineEdit, QMessageBox, QTabWidget, QVBoxLayout, QWidget

import banco
from config import SALDO_INICIAL
from estilo import QSS, aguardando, botao, cabecalho, campo, icone, moeda, rotulo_erro, valor_digitado
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
        cabecalho (layout, "piggy-bank.png", "Abrir conta", f"Toda conta nova começa com {moeda (SALDO_INICIAL)}")
        self.nome = campo (layout, "Nome Completo", "Seu Nome")
        self.email = campo (layout, "Nome Completo")
        self.senha = campo (layout, "Minimo de 6 Caracteres", senha= True)
        self.confirmar = campo (layout, "Canfirmar senha", "Repita a senha")
        self.confirmar.returnPressed.connect (self.cadastrar)
        self.erro = rotulo_erro (layout)
        layout.addWidget (botao ("Cadastrar", self.cadastrar))
        layout.addStretch (1)

    def cadastrar (self):
        nome = self.nome.text().strip()
        email = self.email.text().strip()
        senha = self.senha.text()

        if not nome or not email or not senha:
            self.erro.setText ("Preencha todos os campos")
            return
        if "@" not in email:
            self.erro.setText ("Informe um email válido.")
            return
        if len (senha) < 6:
            self.erro.setText ("A senha precisa ter no mínimo 6 caracteres.")
            return
        if senha != self.confirmar.text():
            self.erro.setText ("As senhas não conferem.")
            return
        try:
            with aguardando():
                banco.cadastrar (email, nome, senha)
        except ErroBanco as e:
            self.erro.setText (str (e))
            return
        self.erro.clear()
        for entrada in (self.nome, self.email, self.senha, self.confirmar):
            entrada.clear()
        QMessageBox.information (self, "Conta Criada com Sucesso", f"Seu saldo é {moeda (SALDO_INICIAL)}.\nFaça Login para continuar",)
        self.janela.login.preencher (email)
        self.janela.setCurrentIndex(LOGIN)

class AbaLogin (QWidget):
    def __init__ (self, janela):
        super().__init__()
        self.janela = janela
        layout = _aba(self)

        cabecalho (layout, "bank.png", "Acesse sua conta", "Informe e-mail e senha")
        self.email = campo (layout, "Email", "email@voce.com")
        self.senha = campo (layout, "Senha", "****", senha= True)
        self.senha.returnPressed.connect (self.entrar)
        mostra = QCheckBox ("Mostrar Senha")
        mostra.toggled.connect (lambda ligado: self.senha.setEchoMode (QLineEdit.Normal if ligado else QLineEdit.Password))
        layout.addWidget.mostra

def main ():
    app = QApplication (sys.argv)
    app.setApplicationName ("TMF")
    app.setFont (QFont ("Segoe UI", 10))