from model.TarefaQuiz import TarefaQuiz
from model.TarefaLeitura import TarefaLeitura
from model.TarefaPratica import TarefaPratica
from model.TarefaProjeto import TarefaProjeto
from model.StatusTarefa import StatusTarefa

print("\n--- Teste Tarefas (script) ---")

# Quiz
q = TarefaQuiz(nota=12, nota_max=10, titulo="Prova 1")  # deve capar em 10/10
print(q.exibir_dados())
print("Progresso Quiz (esperado 100%):", q.progresso()*100, "%")
q.concluir()
print("Após concluir:", q.exibir_dados())
print("Status esperado:", q.status == StatusTarefa.CONCLUIDA)

# Leitura
l = TarefaLeitura(paginas_lidas=20, total_paginas=50, titulo="Capítulo 1")
print(l.exibir_dados())
print("Progresso Leitura (esperado 40%):", l.progresso()*100, "%")

# Prática
p = TarefaPratica(etapas_concluidas=3, total_etapas=6, titulo="Laboratório 1")
print(p.exibir_dados())
print("Progresso Prática (esperado 50%):", p.progresso()*100, "%")

# Projeto
pj = TarefaProjeto(entregas_aprovadas=1, total_entregas=4, titulo="Projeto Final")
print(pj.exibir_dados())
print("Progresso Projeto (esperado 25%):", pj.progresso()*100, "%")
