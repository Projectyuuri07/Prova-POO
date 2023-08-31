from classe import*

def main():
    tarefa = ToDoLIST()
    contid = 0
    sair = False

    while sair == False:
        try:

            limpar()
            print("--|ToDo List|--\n [1]-Adicionar uma tarefa\n [2]-Listar Tarefas\n [3]-Excluir Tarefas\n [4]-Sair")
            opi = int(input("Digite a opção desejada>> "))
            match opi:
                case 1:
                    limpar()
                    print("--|INFORME A TAREFA|--\n\n")
                    contid += 1
                    indice = contid
                    decricao = input(" Escreva a sua tarefa: ")
                    print("\n\n--|TAREFA ADICIONADA COM SUCESSO|--")

                    tarefa.adicionar_tarefa(indice,decricao)
                    parar()
                
                case 2:
                    limpar()
                    print("--|LISTAR TAREFAS|--")
                    tarefa.gettlistar_tarefas()
                    parar()

                case 3:
                    pass

                case 4:
                    print("...Saindo do programa")
                    parar()
                    sair == True
                
                case _:
                    print("Opção invalida\n Escolha apenas as opções acima!")
                    

        except Exception as erro:
            print("Valor invalido")
            print(erro.__class__.__name__)
            print("")