from app.enums import TipoTarefa
from app.tarefa_factory import TarefaFactory
from app.modelos import Aula, Curso, Trilha
from app.strategy_progresso import MediaSimplesStrategy, MediaPonderadaPorCargaStrategy

def montar_demo():
    # Tarefas
    quiz = TarefaFactory.criar(TipoTarefa.QUIZ, nota=8, nota_max=10)
    leitura = TarefaFactory.criar(TipoTarefa.LEITURA, paginas_lidas=20, total_paginas=50)

    # Aula
    aula = Aula("Introdução")
    aula.adicionar_tarefa(quiz)
    aula.adicionar_tarefa(leitura)

    # Curso
    curso = Curso("Python Básico", carga_horas=40)
    curso.adicionar_aula(aula)

    # Trilha
    trilha = Trilha("Trilha de Programação")
    trilha.adicionar_curso(curso)
    return trilha

if __name__ == "__main__":
    trilha = montar_demo()
    print("Progresso (média simples):", f"{trilha.progresso(MediaSimplesStrategy())*100:.1f}%")
    print("Progresso (ponderada por carga):", f"{trilha.progresso(MediaPonderadaPorCargaStrategy())*100:.1f}%")

