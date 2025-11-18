# TarefaEstudo.py
from datetime import datetime
from abc import ABC, abstractmethod
from .StatusTarefa import StatusTarefa

class TarefaEstudo(ABC):
    def __init__(self, titulo, descricao=None, data_realizacao=None, status=StatusTarefa.A_FAZER):
        self.__titulo = titulo
        self.__descricao = descricao
        self.__data_realizacao = None
        if data_realizacao is not None:
            self.data_realizacao = data_realizacao  # usa o setter
        self.__status = status
        self.__concluida = False

    # -------- getters e setters --------
    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, nome):
        self.__titulo = nome.strip().title() if nome else ""

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, desc):
        self.__descricao = desc

    @property
    def data_realizacao(self):
        # expõe a data para leitura
        return self.__data_realizacao

    @data_realizacao.setter
    def data_realizacao(self, data):
        """
        Aceita string no formato 'dd-mm-YYYY' ou um objeto datetime.
        """
        self.__data_realizacao = None
        if data is not None:
            if isinstance(data, str):
                try:
                    self.__data_realizacao = datetime.strptime(data, "%d-%m-%Y")
                except ValueError as e:
                    print(f"Data em formato inválido: {e}")
            elif isinstance(data, datetime):
                self.__data_realizacao = data
            else:
                print("Data inválida")

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, novo_status):
        # espera um membro de StatusTarefa
        self.__status = novo_status

    # -------- outros métodos de domínio --------
    def iniciar_tarefa(self):
        self.__status = StatusTarefa.EM_ANDAMENTO

    def concluir(self):
        self.__concluida = True
        self.__status = StatusTarefa.CONCLUIDA
        self.definir_termino()

    def __str__(self):
        return f"{self.__titulo} [{self.__status.value}]"

    def __eq__(self, outro):
        if isinstance(outro, TarefaEstudo):
            return self.titulo == outro.titulo and self.data_realizacao == outro.data_realizacao
        return False

    # -------- exibição e ponto de extensão --------
    @abstractmethod
    def exibir_dados(self):
        """
        Exibição específica de cada subtipo (quiz, leitura, prática, projeto).
        Subclasses devem complementar, mas podem reutilizar a base abaixo com super().
        """
        base = []
        base.append(f"Tarefa: {self.titulo}")
        if self.descricao:
            base.append(f"Descrição: {self.descricao}")
        data_txt = self.data_realizacao.strftime("%d-%m-%Y") if self.data_realizacao else "Sem data definida"
        base.append(f"Data Realização: {data_txt}")
        base.append(f"Status: {self.status.value}")
        return "\n".join(base)

    @abstractmethod
    def definir_termino(self):
        """
        Atualiza campos quando a tarefa é concluída.
        Ex.: sobrescrever descrição com marcação de atraso, registrar timestamp, etc.
        """
        pass
