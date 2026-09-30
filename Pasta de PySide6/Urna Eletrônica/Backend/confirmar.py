from PySide6.QtWidgets import QMessageBox
from Backend.corrigir import corrigir
from Backend.candidatos import candidatos
from Frontend.tela_confirmacao_candidato import TelaConfirmacaoCandidato
from Backend.eleitor import eleitores

def confirmar(urna):

    if urna.numero_digitado not in candidatos:

        if urna.numero_digitado:
            urna.votos["nulo"] += 1

            QMessageBox.information(
                urna,
                "Voto",
                "Voto nulo!"
            )

            corrigir(urna)

        else:
            QMessageBox.warning(
                urna,
                "Atenção",
                "Digite um número ou escolha BRANCO."
            )

        return

    candidato = candidatos[urna.numero_digitado]

    urna.tela_confirmacao = TelaConfirmacaoCandidato()

    urna.tela_confirmacao.exibir_candidato(
        urna.numero_digitado,
        candidato
    )

    def confirmar_voto():
        urna.votos[urna.numero_digitado] += 1

        QMessageBox.information(
            urna,
            "Voto",
            f"Voto confirmado para {candidato['nome']}!"
        )

        urna.tela_confirmacao.close()
        corrigir(urna)

    def cancelar():
        urna.tela_confirmacao.close()

    urna.tela_confirmacao.confirmar_clicado.connect(confirmar_voto)
    urna.tela_confirmacao.cancelar_clicado.connect(cancelar)

    urna.tela_confirmacao.show()

    def finalizar_votacao(self):
        eleitores[self.titulo_atual]["votou"] = True

        print("Voto registrado com sucesso.")