class Queue:

    def __init__(self):
        self.__elements = []

    def arrive(self, element):
        self.__elements.append(element)

    def attention(self):
        if len(self.__elements) > 0:
            return self.__elements.pop(0)
        else:
            return None
    
    def size(self):
        return len(self.__elements)

    def on_front(self):
        if len(self.__elements) > 0:
            return self.__elements[0]
        else:
            return None
    
    def move_to_end(self):
        element = self.attention()
        if element is not None:
            self.arrive(element)
            

class Cola:

    def __init__(self):
        self.__elementos = []
    
    def arribo(self, elemento):
        self.__elementos.append(elemento)
    
    def atencion(self):
        if len(self.__elementos) > 0:
            return self.__elementos.pop(0)
        else:
            return None
    
    def tamaño(self):
        return len(self.__elementos)
    
    def en_frente(self):
        if len(self.__elementos) > 0:
            return self.__elementos[0]
        else:
            return None
    
    def mover_al_final(self):
        if len(self.__elementos) > 0:
            self.__elementos.append(self.__elementos.pop(0))

