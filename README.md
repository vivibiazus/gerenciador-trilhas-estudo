# Gerenciador de Estudos e Trilhas de Aprendizagem

Organiza **Trilhas → Cursos → Aulas → Tarefas** e aplica POO com padrões para manter o código coeso e flexível.

**Destaques**
- **Factory**: cria tarefas (quiz, leitura, prática, projeto) a partir de um Enum (`TipoTarefa`).
- **Strategy**: calcula o **progresso da trilha** por diferentes métodos (média simples, ponderada por carga horária, por domínios).
- **Extensões**: espaço para lembretes, pré-requisitos e badges (conquistas).

> **Objetivo**: acompanhar a evolução do estudante em trilhas de aprendizagem, trocando o algoritmo de progresso sem alterar as classes de domínio.

---

## Visão geral

- **Estrutura**: uma **Trilha** reúne **Cursos**; cada **Curso** possui **Aulas**; cada **Aula** contém **Tarefas** polimórficas (*Quiz*, *Leitura*, *Prática*, *Projeto*).
- **Cálculo de progresso**: a **Trilha** recebe uma **Strategy** e delega o cálculo, permitindo alternar o método sem mudar as entidades.
- **Padronização**: a **Factory** centraliza a criação das tarefas usando `TipoTarefa`, evitando *ifs* espalhados e erros de digitação.


### Conceitos-chave

- **Enum `TipoTarefa`** — padroniza os tipos de tarefa e evita erros de digitação:
```python
  from app.enums import TipoTarefa

  # Opções: QUIZ, LEITURA, PRATICA, PROJETO
  tipo = TipoTarefa.QUIZ
``` 
- **Factory `TarefaFactory`** — centraliza a criação das tarefas corretas a partir do TipoTarefa:
```python
from app.tarefa_factory import TarefaFactory
from app.enums import TipoTarefa

quiz = TarefaFactory.criar(
    TipoTarefa.QUIZ,
    nota=8,        #nota obtida
    nota_max=10    #nota máxima
)
```
- **Strategy de Progresso** — permite trocar o algoritmo de cálculo de progresso sem alterar Trilha/Curso/Aula:
```python
from app.strategy_progresso import(
   MediaSimplesStrategy,
   MediaPonderadaPorCargaStrategy,
   MediaPorDominioStrategy
)

progresso = trilha.progresso(MediaSimplesStrategy())              # média aritmética simples entre cursos
# progresso = trilha.progresso(MediaPonderadaPorCargaStrategy())  # pondera pelo atributo 'carga_horas' de cada curso
# progresso = trilha.progresso(MediaPorDominioStrategy())         # equilibra por domínios/tipos de tarefas(quiz/leitura/prática/projeto)
```
---
## Diagrama de classes

    classDiagram                  # mantém layout left -> Right
    direction LR

    class Usuario {
      - nome: str
      - trilhas: List<Trilha>
      - badges: List~str~
    }

    class Trilha {
      - nome: str
      - cursos: List<Curso>
      + progresso(strategy: ProgressoStrategy): float
    }

    class Curso {
      - titulo: str
      - aulas: List<Aula>
      - carga_horas: int
      + progresso(): float
    }

    class Aula {
      - titulo: str
      - tarefas: List<TarefaEstudo>
      + progresso(): float
    }

    class TarefaEstudo {
      <<abstract>>
      + progresso(): float
      + resumo(): str
    }

    class TarefaQuiz {
      - nota: float
      - nota_max: float
      + progresso(): float
    }

    class TarefaLeitura {
      - paginas_lidas: int
      - total_paginas: int
      + progresso(): float
    }

    class TarefaPratica {
      - etapas_concluidas: int
      - total_etapas: int
      + progresso(): float
    }

    class TarefaProjeto {
      - entregas_aprovadas: int
      - total_entregas: int
      + progresso(): float
    }

    class TarefaFactory {
      + criar(tipo: TipoTarefa, **kwargs): TarefaEstudo
    }

    class ProgressoStrategy {
      <<interface>>
      + calcular(trilha: Trilha): float
    }

    class MediaSimplesStrategy {
      + calcular(trilha: Trilha): float
    }

    class MediaPonderadaPorCargaStrategy {
      + calcular(trilha: Trilha): float
    }

    class MediaPorDominioStrategy {
      + calcular(trilha: Trilha): float
    }

    class TipoTarefa {
      <<enumeration>>
      QUIZ
      LEITURA
      PRATICA
      PROJETO
    }

### Relacionamentos

#### Multiplicidade
- **Usuário (1)** → **(0..*) Trilha**
- **Trilha (1)** → **(1..*) Curso**
- **Curso (1)** → **(1..*) Aula**
- **Aula (1)** → **(0..*) TarefaEstudo**

#### Herança
- `TarefaQuiz`, `TarefaLeitura`, `TarefaPratica`, `TarefaProjeto` **herdam** de `TarefaEstudo`.
- `MediaSimplesStrategy`, `MediaPonderadaPorCargaStrategy`, `MediaPorDominioStrategy` **implementam** `ProgressoStrategy`.

#### Dependências
- `Trilha` **usa** `ProgressoStrategy` para calcular o progresso.
- `TarefaFactory` **cria** `TarefaEstudo` e **usa** `TipoTarefa` para decidir qual classe instanciar.


--- 
# Estrutura do projeto, pilares de POO e padrões
```text
gerenciador-trilhas-estudo/
├─ README.md
├─ src/
│  └─ app/
│     ├─ enums.py                # Enum: TipoTarefa
│     ├─ modelos.py              # Domínio: Usuario, Trilha, Curso, Aula
│     ├─ tarefas.py              # Abstração/herança/polimorfismo (TarefaEstudo + subclasses)
│     ├─ tarefa_factory.py       # Factory (criação de tarefas)
│     ├─ strategy_progresso.py   # Strategy (algoritmos de progresso)
│     └─ main.py                 # Exemplo de uso (monta demo)
└─ tests/                        # testes 
```

Onde encontram-se os pilares?

**Abstração**
TarefaEstudo define a interface comum (progresso, resumo) sem expor detalhes:
```python
# src/app/tarefas.py
from abc import ABC, abstractmethod

class TarefaEstudo(ABC):
    @abstractmethod
    def progresso(self) -> float: ...
    def resumo(self) -> str:
        return f"{self.__class__.__name__}: {self.progresso()*100:.0f}%"
````
**Herança e Polimorfismo**
Subclasses implementam o cálculo, e Aula/Curso/Trilha usam polimorfismo ao chamar progresso():
```python
# src/app/tarefas.py
class TarefaLeitura(TarefaEstudo):
    def __init__(self, paginas_lidas: int, total_paginas: int):
        self.paginas_lidas = max(0, paginas_lidas)
        self.total_paginas = max(1, total_paginas)
    def progresso(self) -> float:
        return min(1.0, self.paginas_lidas / self.total_paginas)
```
**Encapsulamento**
Cada tarefa mantém e valida seus próprios dados (ex.: limites mínimos/máximos):
```python
class TarefaQuiz(TarefaEstudo):
    def __init__(self, nota: float, nota_max: float = 10.0):
        self.nota = max(0.0, min(nota, nota_max))
        self.nota_max = max(1.0, nota_max)
    def progresso(self) -> float:
        return self.nota / self.nota_max
```
**Padrões**:

`Enum + Factory`
```python
# src/app/enums.py
from enum import Enum
class TipoTarefa(Enum):
    QUIZ="Quiz"; LEITURA="Leitura"; PRATICA="Prática"; PROJETO="Projeto"

# src/app/tarefa_factory.py
from .enums import TipoTarefa
from .tarefas import TarefaQuiz, TarefaLeitura, TarefaPratica, TarefaProjeto, TarefaEstudo

class TarefaFactory:
    @staticmethod
    def criar(tipo: TipoTarefa, **kwargs) -> TarefaEstudo:
        if tipo is TipoTarefa.QUIZ:    return TarefaQuiz(**kwargs)
        if tipo is TipoTarefa.LEITURA: return TarefaLeitura(**kwargs)
        if tipo is TipoTarefa.PRATICA: return TarefaPratica(**kwargs)
        if tipo is TipoTarefa.PROJETO: return TarefaProjeto(**kwargs)
        raise ValueError("Tipo de tarefa inválido")
```
`Strategy`
```python
# src/app/strategy_progresso.py
from abc import ABC, abstractmethod

class ProgressoStrategy(ABC):
    @abstractmethod
    def calcular(self, trilha) -> float: ...

class MediaSimplesStrategy(ProgressoStrategy):
    def calcular(self, trilha) -> float:
        cursos = trilha.cursos
        return 0.0 if not cursos else sum(c.progresso() for c in cursos) / len(cursos)

class MediaPonderadaPorCargaStrategy(ProgressoStrategy):
    def calcular(self, trilha) -> float:
        pares = [(c.progresso(), max(1, c.carga_horas or 1)) for c in trilha.cursos]
        soma_pesos = sum(p for _, p in pares) or 1
        return sum(v*p for v, p in pares) / soma_pesos
```
`Composição (Aula → Tarefas, Curso → Aulas, Trilha → Cursos)`
```python
# src/app/modelos.py
from statistics import mean

class Aula:
    def __init__(self, titulo: str):
        self.titulo = titulo
        self.tarefas = []
    def progresso(self) -> float:
        return 0.0 if not self.tarefas else mean(t.progresso() for t in self.tarefas)
```
