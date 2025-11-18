from .TarefaLeitura import TarefaLeitura
from .TarefaQuiz import TarefaQuiz
from .TarefaPratica import TarefaPratica
from .TarefaProjeto import TarefaProjeto


class TarefaFactory:
    @staticmethod
    def criar(tipo, **kwargs):
        """
        Cria uma tarefa de estudo a partir de um 'tipo' textual.
        Exemplos:
          - criar("leitura", titulo="Capítulo 1", total_paginas=30, paginas_lidas=10)
          - criar("quiz", titulo="Prova 1", nota=8, nota_max=10)
          - criar("pratica", titulo="Lab 1", total_etapas=6, etapas_concluidas=2)
          - criar("projeto", titulo="Projeto Final", total_entregas=4, entregas_aprovadas=1)
        """
        if not tipo:
            raise ValueError("Tipo de tarefa não informado")

        t = str(tipo).strip().lower()

        if t == "leitura":
            kwargs.setdefault("titulo", "Leitura")
            return TarefaLeitura(**kwargs)

        if t == "quiz":
            kwargs.setdefault("titulo", "Quiz")
            return TarefaQuiz(**kwargs)

        if t == "pratica":
            kwargs.setdefault("titulo", "Prática")
            return TarefaPratica(**kwargs)

        if t == "projeto":
            kwargs.setdefault("titulo", "Projeto")
            return TarefaProjeto(**kwargs)

        raise ValueError("Tipo de tarefa inválido. Use: leitura, quiz, pratica ou projeto.")

