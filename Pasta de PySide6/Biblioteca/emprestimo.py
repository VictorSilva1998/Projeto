from dataclasses import dataclass
from datetime import date, timedelta
from typing import Optional

@dataclass
class Emprestimo:
    titulo_livro: str
    data_emprestimo: date
    data_prevista: Optional [date] = None
    data_devolucao: Optional [date] = None
    prazo: 14

    def __post_init__ (self):
        if self.data_prevista is None:
            self.data_prevista = self.data_emprestimo + timedelta (days = self.prazo)

    def registrar_devolucao (self, devolucao = date) -> None:
        self.data_devolucao = devolucao