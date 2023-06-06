from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.req1 = list()

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self.req1)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self.req1.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        return self.req1.pop(0)

    def search(self, index):
        """Aqui irá sua implementação"""
        if (index < 0) or (index >= len(self.req1)):
            raise IndexError("Índice Inválido ou Inexistente")
        return self.req1[index]
