import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from app.modelos import Aula, Curso, Trilha
from app.tarefas import TarefaLeitura, TarefaQuiz
from app.strategy_progresso import MediaSimplesStrategy, MediaPonderadaPorCargaStrategy

def montar_trilha_para_testes():
    # Curso 1: progresso 0.5, carga 10
    a1 = Aula("A1"); a1.adicionar_tarefa(TarefaLeitura(5, 10))  # 0.5
    c1 = Curso("C1", carga_horas=10); c1.adicionar_aula(a1)

    # Curso 2: progresso 1.0, carga 30
    a2 = Aula("A2"); a2.adicionar_tarefa(TarefaQuiz(10, 10))    # 1.0
    c2 = Curso("C2", carga_horas=30); c2.adicionar_aula(a2)

    t = Trilha("T")
    t.adicionar_curso(c1)
    t.adicionar_curso(c2)
    return t

def test_media_simples_strategy():
    trilha = montar_trilha_para_testes()
    valor = trilha.progresso(MediaSimplesStrategy())
    assert abs(valor - 0.75) < 1e-6  # (0.5 + 1.0) / 2

def test_media_ponderada_por_carga_strategy():
    trilha = montar_trilha_para_testes()
    valor = trilha.progresso(MediaPonderadaPorCargaStrategy())
    # (0.5*10 + 1.0*30) / (10+30) = (5 + 30) / 40 = 0.875
    assert abs(valor - 0.875) < 1e-6
