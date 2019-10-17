import random

class Dado:
    def __init__ (self):
        self.dado=0
    def tirarDado(self):
        self.dado=random.randint(1, 6)

    def getDado(self):
        return self.dado
