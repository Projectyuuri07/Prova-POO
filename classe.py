import os

def limpar():
    os.system("cls")

def parar():
    os.system("pause")

class ToDoLIST:
    def __init__(self):
        self.lista = {}

    def adicionar_tarefa(self, indice, descricao: str,):
        self.descricao = descricao
        self.indice = indice
        self.lista[self.indice] =[ self.descricao]

    def excluir_tarefa(self, indice: int):
        if indice in self.lista


    def gettlistar_tarefas(self):
        for chave,valor in self.lista.items():
            print(f"{chave}. {valor}\n")



