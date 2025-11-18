import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from app.enums import TipoTarefa
from app.tarefa_factory import TarefaFactory
from app.tarefas import TarefaQuiz, TarefaLeitura, TarefaPratica, TarefaProjeto

def test_factory_cria_quiz():
    obj = TarefaFactory.criar(TipoTarefa.QUIZ, nota=7, nota_max=10)
    assert isinstance(obj, TarefaQuiz)

def test_factory_cria_leitura():
    obj = TarefaFactory.criar(TipoTarefa.LEITURA, paginas_lidas=5, total_paginas=20)
    assert isinstance(obj, TarefaLeitura)

def test_factory_cria_pratica():
    obj = TarefaFactory.criar(TipoTarefa.PRATICA, etapas_concluidas=2, total_etapas=5)
    assert isinstance(obj, TarefaPratica)

def test_factory_cria_projeto():
    obj = TarefaFactory.criar(TipoTarefa.PROJETO, entregas_aprovadas=1, total_entregas=3)
    assert isinstance(obj, TarefaProjeto)
