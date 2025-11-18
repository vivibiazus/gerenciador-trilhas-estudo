import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from statistics import mean
from app.modelos import Aula, Curso, Trilha
from app.tarefas import TarefaLeitura, TarefaQuiz

def test_aula_progresso_media_tarefas():
    aula = Aula("A1")
    aula.adicionar_tarefa(TarefaLeitura(5, 10))  # 0.5
    aula.adicionar_tarefa(TarefaQuiz(8, 10))     # 0.8
    assert abs(aula.progresso() - mean([0.5, 0.8])) < 1e-6

def test_curso_progresso_media_aulas():
    a1 = Aula("A1"); a1.adicionar_tarefa(TarefaLeitura(5, 10))  # 0.5
    a2 = Aula("A2"); a2.adicionar_tarefa(TarefaQuiz(10, 10))    # 1.0

    curso = Curso("C1", carga_horas=20)
    curso.adicionar_aula(a1)
    curso.adicionar_aula(a2)

    assert abs(curso.progresso() - 0.75) < 1e-6  # média de 0.5 e 1.0
