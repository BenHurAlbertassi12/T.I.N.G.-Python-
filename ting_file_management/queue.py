from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.req1 = list()
    # inicializa a estrutura de dados self.req1 como uma lista vazia

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self.req1)
    # obter o tamanho da lista.

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self.req1.append(value)
    # adiciona um novo value ao final da lista

    def dequeue(self):
        """Aqui irá sua implementação"""
        return self.req1.pop(0)
    # adiciona um novo value ah estrutura de dados self.req1
    # no final da lista.

    def search(self, index):
        """Aqui irá sua implementação"""
        if (index < 0) or (index >= len(self.req1)):
            # se o index for negativo ou maior ou igual ao tamanho da fila
            raise IndexError("Índice Inválido ou Inexistente")
            # retorna a mensagem de erro
        return self.req1[index]
        # se pssar na validação retorna a posição do index na estrutra self.req
