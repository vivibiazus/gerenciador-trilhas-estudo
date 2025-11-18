from statistics import mean
from .tarefas import TarefaEstudo

class Aula:
    def __init__(self, titulo):
        self.titulo = str(titulo)
        self.tarefas = []  # lista de TarefaEstudo

    def adicionar_tarefa(self, tarefa):
        if not isinstance(tarefa, TarefaEstudo):
            raise TypeError("tarefa deve herdar de TarefaEstudo")
        self.tarefas.append(tarefa)

    def progresso(self):
        if not self.tarefas:
            return 0.0
        return mean(t.progresso() for t in self.tarefas)


class Curso:
    def __init__(self, titulo, carga_horas=0):
        self.titulo = str(titulo)
        self.carga_horas = int(carga_horas) if carga_horas else 0
        self.aulas = []  # lista de Aula

    def adicionar_aula(self, aula):
        if not isinstance(aula, Aula):
            raise TypeError("aula deve ser do tipo Aula")
        self.aulas.append(aula)

    def progresso(self):
        if not self.aulas:
            return 0.0
        return mean(a.progresso() for a in self.aulas)


class Trilha:
    def __init__(self, nome):
        self.nome = str(nome)
        self.cursos = []  # lista de Curso

    def adicionar_curso(self, curso):
        if not isinstance(curso, Curso):
            raise TypeError("curso deve ser do tipo Curso")
        self.cursos.append(curso)

    def progresso(self, strategy):
        """Delegação para a estratégia escolhida."""
        return strategy.calcular(self)

