from animal import Animal
from bird import Bird
from cow import Cow
from fish import Fish


def main():
    # Erzeuge ein "abstraktes" Tier. Wie soll sich das bewegen?
    #animal = Animal("was genau?")
    #animal.move()
    # Erzeuge einen Vogel
    bird = Bird("Vogel", "Kudu")
    bird.move()
    # Erzeugt einen Fisch
    fish = Fish("Fisch", "Nemo")
    fish.move()
    # Erzeugt eine Kuh
    cow = Cow("Kuh", "Ziba")
    cow.move()
    #
    # Eine kleine Demo was noch möglich ist.
    print("\n\nDemo zu Polymorphie")
    # Alle Objekt in eine Liste (Sammlung) stecken.
    animals = [bird, fish, cow]
    # animals enthält verschiedene Objekte, die aber alle die Fähigkeit move() haben.
    # Jedes Objekt der konkreten Tiere erbt von Animal, ist somit auch vom Typ Animal.
    # Nun können alle Objekte mit der Sicht - der Brille - "Animal" betrachtet werden.
    # Das ermöglicht es, alle Objekte als gleich - also vom gleichen Typ - zu behandeln.
    # Und somit können alle in einer for-Schleife abgearbeitet werden. Aber...
    # ...jedes Objekt kennt seine spezifische move()-Methode und führt diese aus und
    # nicht jene der Klasse Animal. Das ist Polymorphie.
    for animal in animals:
        animal.move()

    # stark...oder?


if __name__ == "__main__":
    main()
