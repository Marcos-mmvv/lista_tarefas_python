# Lista de tarefas

lista_tarefas = []

while True:
    tarefa = input('Insira a tarefa ou deixe vazio para encerrar o cadastro e exibir a lista: ').capitalize()

    if tarefa != '':
        lista_tarefas.append(tarefa)
        continue
    else:
        break

for tarefa in range(len(lista_tarefas)):
    print(f' {tarefa +1}º Tarefa a fazer - {lista_tarefas[tarefa]}')
    

