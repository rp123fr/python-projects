class Animal():
    def __init__(self,name):
        self.a_name=name
    def make_sound(self):
        pass
    def Move(self):
        pass
        

class Dog(Animal):
    def make_sound(self):
        self.a_sound="bhou-bhou"
        return self.a_sound
    def Move(self):
       self.a_move="run"
       return self.a_move

class Bird(Animal):
    def make_sound(self):
        self.a_sound="chirpp" 
        return self.a_sound
    def Move(self):
        self.a_move="fly"
        return self.a_move

class Fish(Animal):
    def make_sound(self):
        self.a_sound="blub"
        return self.a_sound
    def Move(self):
        self.a_move="swim"
        return self.a_move
       


class Zoo:
    def __init__(self):
        self.animals = []   # empty list to start

    def add_animal(self, animal):
        self.animals.append(animal)
        

    def make_all_sounds(self):
        # loop through self.animals and call make_sound() on each
        for x in self.animals:
            print(f"{x.a_name} sounds like {x.make_sound()}")

    def move_all(self):
        for y in self.animals:
            print(f"{y.a_name}:{y.Move()}")



zoo = Zoo()
zoo.add_animal(Dog("Rex"))
zoo.add_animal(Bird("Tweety"))
zoo.add_animal(Fish("Gold"))
zoo.make_all_sounds()
zoo.move_all()