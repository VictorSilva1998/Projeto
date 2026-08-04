from dataclasses import dataclass, field
from typing import List

@dataclass
class Aluno:
    nome: str
    cpf: str
    matricula: str
    limite: int = 3
    emprestados: List[str] = field(default_factory=list)

    def pegar_emprestado(self, titulo_livro: str) -> bool:
        if len(self.emprestados) < self.limite:
            self.emprestados.append(titulo_livro)
            return True
        return False