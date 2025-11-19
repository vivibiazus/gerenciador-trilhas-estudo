from .TipoTarefaEstudo import TipoTarefaEstudo
from .TarefaLeitura import TarefaLeitura
from .TarefaQuiz import TarefaQuiz
from .TarefaPratica import TarefaPratica
from .TarefaProjeto import TarefaProjeto


class TarefaFactory:
    @staticmethod
    def criar(tipo, **kwargs):
        """
        Cria uma tarefa de estudo de acordo com o 'tipo'.
        Aceita:
          - string: "leitura", "quiz", "pratica", "projeto"
          - enum:   TipoTarefaEstudo.LEITURA, QUIZ, PRATICA, PROJETO

        Parâmetros esperados por tipo:
          leitura -> titulo, total_paginas, (paginas_lidas=0), descricao, data_realizacao
          quiz    -> titulo, nota, (nota_max=10), descricao, data_realizacao
          pratica -> titulo, total_etapas, (etapas_concluidas=0), descricao, data_realizacao
          projeto -> titulo, total_entregas, (entregas_aprovadas=0), descricao, data_realizacao
        """
        if not tipo:
            raise ValueError("Tipo de tarefa não informado.")

        # normaliza o tipo (enum ou string) para minúsculas
        if isinstance(tipo, TipoTarefaEstudo):
            chave = tipo.name.lower()  # "LEITURA" -> "leitura"
        else:
            chave = str(tipo).strip().lower()

        # ---- LEITURA --------------------------------------------------------
        if chave == "leitura":
            if kwargs.get("total_paginas") is None:
                raise ValueError("Para 'leitura', informe 'total_paginas'.")
            kwargs.setdefault("titulo", "Leitura")
            kwargs.setdefault("paginas_lidas", 0)
            return TarefaLeitura(
                titulo=kwargs.get("titulo"),
                total_paginas=kwargs.get("total_paginas"),
                paginas_lidas=kwargs.get("paginas_lidas"),
                descricao=kwargs.get("descricao"),
                data_realizacao=kwargs.get("data_realizacao"),
            )

        # ---- QUIZ -----------------------------------------------------------
        if chave == "quiz":
            if kwargs.get("nota") is None:
                raise ValueError("Para 'quiz', informe 'nota'.")
            kwargs.setdefault("titulo", "Quiz")
            kwargs.setdefault("nota_max", 10)
            return TarefaQuiz(
                titulo=kwargs.get("titulo"),
                nota=kwargs.get("nota"),
                nota_max=kwargs.get("nota_max"),
                descricao=kwargs.get("descricao"),
                data_realizacao=kwargs.get("data_realizacao"),
            )

        # ---- PRÁTICA --------------------------------------------------------
        if chave == "pratica":
            if kwargs.get("total_etapas") is None:
                raise ValueError("Para 'pratica', informe 'total_etapas'.")
            kwargs.setdefault("titulo", "Prática")
            kwargs.setdefault("etapas_concluidas", 0)
            return TarefaPratica(
                titulo=kwargs.get("titulo"),
                total_etapas=kwargs.get("total_etapas"),
                etapas_concluidas=kwargs.get("etapas_concluidas"),
                descricao=kwargs.get("descricao"),
                data_realizacao=kwargs.get("data_realizacao"),
            )

        # ---- PROJETO --------------------------------------------------------
        if chave == "projeto":
            if kwargs.get("total_entregas") is None:
                raise ValueError("Para 'projeto', informe 'total_entregas'.")
            kwargs.setdefault("titulo", "Projeto")
            kwargs.setdefault("entregas_aprovadas", 0)
            return TarefaProjeto(
                titulo=kwargs.get("titulo"),
                total_entregas=kwargs.get("total_entregas"),
                entregas_aprovadas=kwargs.get("entregas_aprovadas"),
                descricao=kwargs.get("descricao"),
                data_realizacao=kwargs.get("data_realizacao"),
            )

        # ---- tipo inválido --------------------------------------------------
        raise ValueError("Tipo de tarefa inválido. Use: leitura, quiz, pratica ou projeto.")



