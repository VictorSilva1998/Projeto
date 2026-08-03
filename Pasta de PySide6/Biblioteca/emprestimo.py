from dataclasses import dataclass
from datetime import date

@dataclass
class emprestimo:
    data_emprestimo: date
    data_prevista: date
    data_devolucao: date | None
    devolvido: bool

    def registrar_devolucao (self) -> date: