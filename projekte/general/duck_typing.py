# Beispiele für Duck Typing
class Duck:
    def fly(self):
        print("flying")

    def swim(self):
        print("swimming")

# Klassendeklaration nur mit der Methode fly()
class Albatross:
    def fly(self):
        print("flying")

# Initialisierung einer Liste mit je einer Instanz der beiden Klassen
birds = [Duck(), Albatross()]

# Foreach-Schleife mit Ducktyping
for bird in birds:
    print(type(bird))
    bird.fly()
    bird.swim()