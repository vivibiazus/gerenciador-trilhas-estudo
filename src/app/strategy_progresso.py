from abc import ABC, abstractmethod

class ProgressoStrategy(ABC):
    @abstractmethod
    def calcular(self, trilha):
        raise NotImplementedError


class MediaSimplesStrategy(ProgressoStrategy):
    def calcular(self, trilha):
        cursos = trilha.cursos
        if not cursos:
            return 0.0
        return sum(c.progresso() for c in cursos) / float(len(cursos))


class MediaPonderadaPorCargaStrategy(ProgressoStrategy):
    def calcular(self, trilha):
        if not trilha.cursos:
            return 0.0
        soma_pesos = 0
        soma = 0.0
        for c in trilha.cursos:
            peso = c.carga_horas if c.carga_horas else 1
            soma += c.progresso() * peso
            soma_pesos += peso
        if soma_pesos == 0:
            return 0.0
        return soma / float(soma_pesos)


class MediaPorDominioStrategy(ProgressoStrategy):
    """
    Exemplo simplificado: faz média das parcelas de cada tipo de tarefa.
    Aqui usamos apenas a média dos cursos (poderia ser expandido por domínio real).
    """
    def calcular(self, trilha):
        if not trilha.cursos:
            return 0.0
        return sum(c.progresso() for c in trilha.cursos) / float(len(trilha.cursos))

