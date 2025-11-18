from abc import ABC, abstractmethod

class TarefaEstudo(ABC):
    @abstractmethod
    def progresso(self):
        """Retorna um valor de 0.0 a 1.0 representando o progresso."""
        raise NotImplementedError

    def resumo(self):
        return f"{self.__class__.__name__}: {self.progresso() * 100:.0f}%"


class TarefaQuiz(TarefaEstudo):
    def __init__(self, nota, nota_max=10.0):
        self.nota_max = float(nota_max)
        if self.nota_max < 1.0:
            self.nota_max = 1.0
        self.nota = float(nota)
        if self.nota < 0.0:
            self.nota = 0.0
        if self.nota > self.nota_max:
            self.nota = self.nota_max

    def progresso(self):
        return self.nota / self.nota_max


class TarefaLeitura(TarefaEstudo):
    def __init__(self, paginas_lidas, total_paginas):
        self.total_paginas = int(total_paginas)
        if self.total_paginas < 1:
            self.total_paginas = 1
        self.paginas_lidas = int(paginas_lidas)
        if self.paginas_lidas < 0:
            self.paginas_lidas = 0
        if self.paginas_lidas > self.total_paginas:
            self.paginas_lidas = self.total_paginas

    def progresso(self):
        return float(self.paginas_lidas) / float(self.total_paginas)


class TarefaPratica(TarefaEstudo):
    def __init__(self, etapas_concluidas, total_etapas):
        self.total_etapas = int(total_etapas)
        if self.total_etapas < 1:
            self.total_etapas = 1
        self.etapas_concluidas = int(etapas_concluidas)
        if self.etapas_concluidas < 0:
            self.etapas_concluidas = 0
        if self.etapas_concluidas > self.total_etapas:
            self.etapas_concluidas = self.total_etapas

    def progresso(self):
        return float(self.etapas_concluidas) / float(self.total_etapas)


class TarefaProjeto(TarefaEstudo):
    def __init__(self, entregas_aprovadas, total_entregas):
        self.total_entregas = int(total_entregas)
        if self.total_entregas < 1:
            self.total_entregas = 1
        self.entregas_aprovadas = int(entregas_aprovadas)
        if self.entregas_aprovadas < 0:
            self.entregas_aprovadas = 0
        if self.entregas_aprovadas > self.total_entregas:
            self.entregas_aprovadas = self.total_entregas

    def progresso(self):
        return float(self.entregas_aprovadas) / float(self.total_entregas)

