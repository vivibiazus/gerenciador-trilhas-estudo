from datetime import datetime
from .TarefaEstudo import TarefaEstudo
from .StatusTarefa import StatusTarefa


class TarefaLeitura(TarefaEstudo):
    def __init__(self, titulo, total_paginas, paginas_lidas=0, descricao=None,
                 data_realizacao=None, status=StatusTarefa.A_FAZER):
        super().__init__(titulo=titulo, descricao=descricao,
                         data_realizacao=data_realizacao, status=status)
        self.total_paginas = total_paginas
        self.paginas_lidas = paginas_lidas

    # --- getters e setters ---

    @property
    def total_paginas(self):
        return self.__total_paginas

    @total_paginas.setter
    def total_paginas(self, total):
        try:
            total_int = int(total)
            self.__total_paginas = total_int if total_int > 0 else 1
        except (TypeError, ValueError):
            self.__total_paginas = 1

    @property
    def paginas_lidas(self):
        return self.__paginas_lidas

    @paginas_lidas.setter
    def paginas_lidas(self, lidas):
        try:
            lidas_int = int(lidas)
        except (TypeError, ValueError):
            lidas_int = 0

        # mantém dentro do intervalo [0, total_paginas]
        if lidas_int < 0:
            lidas_int = 0
        if hasattr(self, "_TarefaLeitura__total_paginas") and lidas_int > self.__total_paginas:
            lidas_int = self.__total_paginas
        self.__paginas_lidas = lidas_int

    # --- métodos auxiliares ---

    def __str__(self):
        return f"[Leitura] {super().__str__()}"

    def exibir_dados(self):
        base = super().exibir_dados()
        info = (
            f"Tipo: Leitura\n"
            f"Páginas lidas: {self.paginas_lidas} de {self.total_paginas}\n"
        )
        return f"{base}\n{info}"

    def definir_termino(self):
        """Conclui a leitura marcando data e status."""
        self.data_realizacao = datetime.now()
        self.status = StatusTarefa.CONCLUIDA

