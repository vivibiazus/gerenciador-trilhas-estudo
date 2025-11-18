import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from app.tarefas import TarefaQuiz, TarefaLeitura, TarefaPratica, TarefaProjeto

def test_quiz_progress_limits():
    q = TarefaQuiz(nota=12, nota_max=10)  # deve capar em 10/10
    assert q.progresso() == 1.0

    q2 = TarefaQuiz(nota=-5, nota_max=10)  # não pode negativo
    assert q2.progresso() == 0.0

def test_leitura_progress():
    l = TarefaLeitura(paginas_lidas=20, total_paginas=40)
    assert abs(l.progresso() - 0.5) < 1e-6

def test_pratica_progress():
    p = TarefaPratica(etapas_concluidas=3, total_etapas=6)
    assert abs(p.progresso() - 0.5) < 1e-6

def test_projeto_progress():
    pj = TarefaProjeto(entregas_aprovadas=1, total_entregas=4)
    assert abs(pj.progresso() - 0.25) < 1e-6

