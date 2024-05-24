# Lista de tarefas
import os


lista_tarefas = []

while True:
    tarefa = input('Insira a tarefa ou deixe vazio para encerrar o cadastro e exibir a lista: ').capitalize()
    
    if tarefa != '':
        lista_tarefas.append(tarefa)
        continue
    else:
        break

os.system('cls')

print(f'{'-'*30} LISTA DE TAREFAS {'-'*30}\n')

from datetime import date

data_atual = date.today()
print(f'Tarefas do dia - {data_atual}\n')

for tarefa in range(len(lista_tarefas)):
    print(f' {tarefa +1}º Tarefa a fazer - {lista_tarefas[tarefa]}')
    


