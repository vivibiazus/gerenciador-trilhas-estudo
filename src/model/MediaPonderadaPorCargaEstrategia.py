from .EstrategiaProgresso import EstrategiaProgresso

class MediaPonderadaPorCargaEstrategia(EstrategiaProgresso):
    def calcular(self, trilha):
        cursos = trilha.cursos
        if not cursos:
            return 0.0
        soma = 0.0
        soma_pesos = 0
        for c in cursos:
            peso = c.carga_horas if c.carga_horas else 1
            soma += c.progresso() * peso
            soma_pesos += peso
        if soma_pesos == 0:
            return 0.0
        return soma / float(soma_pesos)

