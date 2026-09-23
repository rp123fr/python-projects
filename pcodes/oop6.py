from abc import ABC,abstractmethod#abstract base class 
class Animal(ABC):  
    def eat(self):
        print("eating...")

    @abstractmethod
    def die(self):
        print("die")

class Bird(Animal): 
    def fly(self):
        print("flying...")
    def die(self):
            print("die")

class Fish():
    def swim(self):
        print("swimming...")



