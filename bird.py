from animal import Animal


class Bird(Animal):

    def __init__(self, species, name):
        super().__init__(species)
        self.__name = name

    def move(self):
        print(f'{self._species} mit Name {self.__name} fliegt')