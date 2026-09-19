tarefas = []

print("Bem-vindo(a) à Zara, sua assistente pessoal de tarefas.")
nome_usuario = input("Qual é o seu nome? ")

while True:
    print(f"\n=====================================")
    print(f"Olá, {nome_usuario}! O que deseja fazer?")
    print("1 - Ver tarefas")
    print("2 - Adicionar tarefa")
    print("3 - Remover tarefa")
    print("4 - Marcar como concluída")

    print("0 - Sair")

    opcao = input("\nDigite a opção desejada: ")

    match opcao:
        case "1":
            print("\n--- SUAS TAREFAS ---")
            if len(tarefas) == 0:
                print("Nenhuma tarefa encontrada.")
            else:
                for i in range(len(tarefas)):
                    if "concluida" not in tarefas[i]:
                        tarefas[i]["concluida"] = False

                    if tarefas[i]["concluida"] == True:
                        status = "Concluída"
                    else:
                        status = "Pendente"

                    print(f"{i+1}º - {tarefas[i]['nome']} (Prioridade: {tarefas[i]['prioridade']}) ({status})")

        case "2":
            print("\n--- ADICIONAR TAREFA ---")
            nome_tarefa = input("Digite o nome da tarefa: ")

            print("Prioridades: 1 para Alta, 2 para Média, 3 para Baixa")
            opcao_prioridade = input("Escolha a prioridade: ")

            if opcao_prioridade == "1":
                prioridade = "Alta"
            elif opcao_prioridade == "2":
                prioridade = "Média"
            else:
                prioridade = "Baixa"

            nova_tarefa = {
                "nome": nome_tarefa,
                "prioridade": prioridade,
                "concluida": False,
            }
            tarefas.append(nova_tarefa)
            print("Tarefa adicionada com sucesso!")

        case "3":
            print("\n--- REMOVER TAREFA ---")
            if len(tarefas) == 0:
                print("Nenhuma tarefa para remover.")
            else:
                for i in range(len(tarefas)):
                    print(f"{i+1} - {tarefas[i]['nome']}")

                indice = int(input("Digite o número da tarefa que deseja remover: "))

                if indice > 0 and indice <= len(tarefas):
                    tarefas.pop(indice - 1)
                    print("Tarefa removida!")
                else:
                    print("Número inválido.")

        case "4":
            print("\n--- MARCAR COMO CONCLUÍDA ---")
            if len(tarefas) == 0:
                print("Nenhuma tarefa cadastrada.")
            else:
                for i in range(len(tarefas)):
                    if "concluida" not in tarefas[i]:
                        tarefas[i]["concluida"] = False
                    status = "Concluída" if tarefas[i]["concluida"] else "Pendente"
                    print(f"{i+1} - {tarefas[i]['nome']} ({status})")

                indice = int(input("Digite o número da tarefa: "))

                if indice > 0 and indice <= len(tarefas):
                    if "concluida" not in tarefas[indice - 1]:
                        tarefas[indice - 1]["concluida"] = False

                    tarefas[indice - 1]["concluida"] = not tarefas[indice - 1]["concluida"]
                    print("Status da tarefa atualizado!")
                else:
                    print("Número inválido.")

        case "0":
            print(f"\nAté logo, {nome_usuario}! Saindo do programa...")
            break

        case _:
            print("\nOpção inválida. Por favor, digite um número de 0 a 6.")
