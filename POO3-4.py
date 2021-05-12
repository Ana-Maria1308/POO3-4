#2
class Impartire:
    def __init__(self, deimpartit, impartitor):
        self.__deimpartit = deimpartit
        self.__impartitor = impartitor

    def executa(self):
        return self.__deimpartit / self.__impartitor


obj = Impartire(9, 3)
print(obj.executa())
#3
class Impartire:
    def __init__(self, deimpartit, impartitor):
        self.__deimpartit = None
        self.__impartitor = None

        self.set_deimpartit(deimpartit)
        self.set_impartitor(impartitor)

    def get_deimpartit(self):
        return self.__deimpartit

    def set_deimpartit(self, valoare):
        self.__deimpartit = valoare

    def get_impartitor(self):
        return self.__impartitor

    def set_impartitor(self, valoare):
        if valoare == 0:
            raise ValueError('Valoarea trebuie sa fie diferita de zero')
        self.__impartitor = valoare

    def executa(self):
        return self.__deimpartit / self.__impartitor


obj = Impartire(9, 3)
print(obj.executa())

print(obj.get_deimpartit(), obj.get_impartitor())
