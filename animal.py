from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, species):
        self._species = species
    @abstractmethod
    def move(self):
        print('Tier weiss nicht konkret, wie es sich bewegen soll')