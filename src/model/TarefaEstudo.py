from datetime import datetime
from abc import ABC, abstractmethod
from .StatusTarefa import StatusTarefa


class TarefaEstudo(ABC):
    def __init__(self, titulo, descricao=None, data_realizacao=None, status=StatusTarefa.A_FAZER):
        self.__titulo = titulo
        self.__descricao = descricao
        self.__data_realizacao = None  # inicializa
        if data_realizacao is not None:
            self.data_realizacao = data_realizacao
        self.status = status
        self.__concluida = False

    # --- encapsulamento: getters e setters ---

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, nome):
        self.__titulo = nome.strip().title() if nome else None

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, desc):
        self.__descricao = desc

    @property
    def data_realizacao(self):
        return self.__data_realizacao

    @data_realizacao.setter
    def data_realizacao(self, data):
        """Aceita string 'dd-mm-YYYY' ou datetime."""
        self.__data_realizacao = None
        if data is not None:
            try:
                if isinstance(data, str):
                    self.__data_realizacao = datetime.strptime(data, "%d-%m-%Y")
                elif isinstance(data, datetime):
                    self.__data_realizacao = data
                else:
                    print("Data inválida")
            except ValueError as e:
                print(f"Data em formato inválido: {e}")

    # --- outros métodos  ---

    def concluir(self):
        self.__concluida = True
        self.status = StatusTarefa.CONCLUIDA
        self.definir_termino()

    def iniciar_estudo(self):
        self.status = StatusTarefa.EM_ANDAMENTO

    def __str__(self):
        return f"{self.__class__.__name__}: {self.__titulo} [{self.status.value}]"

    def __eq__(self, outro):
        if isinstance(outro, TarefaEstudo):
            return self.titulo == outro.titulo and self.data_realizacao == outro.data_realizacao
        return False

    @abstractmethod
    def exibir_dados(self):
        """Retorna texto com dados da tarefa (sobrescrito nas filhas)."""
        descricao = f"Descrição: {self.descricao}\n" if self.descricao else ""
        data = f"{self.data_realizacao.strftime('%d-%m-%Y')}" if self.data_realizacao else "Sem data definida"
        return (f"Tarefa: {self.titulo}\n"
                f"{descricao}"
                f"Status: {self.status.value}\n"
                f"Data Realização: {data}")

    @abstractmethod
    def definir_termino(self):
        """Define regras de término"""
        pass
