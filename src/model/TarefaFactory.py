from .enums import TipoTarefa
from .tarefas import (
    TarefaEstudo, TarefaQuiz, TarefaLeitura, TarefaPratica, TarefaProjeto
)

class TarefaFactory:
    @staticmethod
    def criar(tipo, **kwargs):
        """Cria a tarefa correta a partir do Enum TipoTarefa."""
        mapa = {
            TipoTarefa.QUIZ: TarefaQuiz,
            TipoTarefa.LEITURA: TarefaLeitura,
            TipoTarefa.PRATICA: TarefaPratica,
            TipoTarefa.PROJETO: TarefaProjeto,
        }
        cls = mapa.get(tipo)
        if not cls:
            raise ValueError("Tipo de tarefa inválido")
        return cls(**kwargs)

