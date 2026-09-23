#multi-level inheritance 
class Animal():
    def eat(self):
        print("eating...")

class Bird(Animal): #inheriting attributes from class animal to class bird
    def fly(self):
        print("flying...")

class Eagle(Bird): #suppose we want to inherit attributes of class animal and bird in this class then
    def breed(self): #there is no need to inherit both the class we shall simply inherit class bird 
        print("breed:black hawk eagle") #since class bird has already inherited class animal 
#this is called multi-level inheritance
a=Animal()
a.eat()

b=Bird()
b.fly()

e=Eagle()
e.breed()
e.fly()  