from datetime import datetime
from .TarefaEstudo import TarefaEstudo
from .StatusTarefa import StatusTarefa


class TarefaPratica(TarefaEstudo):
    def __init__(self, titulo, total_etapas, etapas_concluidas=0, descricao=None,
                 data_realizacao=None, status=StatusTarefa.A_FAZER):
        super().__init__(titulo=titulo, descricao=descricao,
                         data_realizacao=data_realizacao, status=status)
        self.total_etapas = total_etapas
        self.etapas_concluidas = etapas_concluidas

    # --- getters e setters ---

    @property
    def total_etapas(self):
        return self.__total_etapas

    @total_etapas.setter
    def total_etapas(self, v):
        try:
            v = int(v)
        except (TypeError, ValueError):
            v = 1
        if v < 1:
            v = 1
        self.__total_etapas = v
        # revalida concluídas se já existir
        if hasattr(self, "_TarefaPratica__etapas_concluidas") and self.__etapas_concluidas > v:
            self.__etapas_concluidas = v

    @property
    def etapas_concluidas(self):
        return self.__etapas_concluidas

    @etapas_concluidas.setter
    def etapas_concluidas(self, v):
        try:
            v = int(v)
        except (TypeError, ValueError):
            v = 0
        if v < 0:
            v = 0
        if hasattr(self, "_TarefaPratica__total_etapas") and v > self.__total_etapas:
            v = self.__total_etapas
        self.__etapas_concluidas = v

    # --- métodos especiais/auxiliares ---

    def __str__(self):
        return f"[Prática] {super().__str__()}"

    def exibir_dados(self):
        base = super().exibir_dados()
        linhas = [
            base,
            "Tipo: Prática",
            f"Etapas: {self.etapas_concluidas}/{self.total_etapas}",
        ]
        return "\n".join(linhas)

    def definir_termino(self):
        """Conclui a prática marcando data e status."""
        self.data_realizacao = datetime.now()
        self.status = StatusTarefa.CONCLUIDA

