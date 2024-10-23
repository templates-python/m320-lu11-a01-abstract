from animal import Animal
from bird import Bird
from cow import Cow
from fish import Fish


class TestAnimals:

    def test_animal(self):
        try:
            animal = Animal('unknown')
            animal.move()
            assert False
        except TypeError:
            assert True

    def test_bird(self, capsys):
        animal = Bird('Vogel', 'Kudu')
        animal.move()
        captured = capsys.readouterr()
        assert captured.out == 'Vogel mit Name Kudu fliegt\n'

    def test_cow(self, capsys):
        animal = Cow('Kuh', 'Julia')
        animal.move()
        captured = capsys.readouterr()
        assert captured.out == 'Kuh mit Name Julia läuft\n'

    def test_fish(self, capsys):
        animal = Fish('Fisch', 'Momo')
        animal.move()
        captured = capsys.readouterr()
        assert captured.out == 'Fisch mit Name Momo schwimmt\n'