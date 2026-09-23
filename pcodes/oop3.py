class Human():

    def __init__(self,f,l,a): #passing three parameters inside this magic method 
        self.first_name=f
        self.last_name=l
        self.__age=a        #to make a attribute non-accesible outside class we use double  underscore before it

    def __str__(self):   #this magic method is used to print without calling it. 
        return "i am a human"
 
user=Human("light","yagami",18)
you=Human("L","lawliet",24)

#suppose we need to add aa unique attribute to a particular object we could this by:
user.ability="kira"
#print(user.age) #this will throw error sice we made age non-accesible outside class

print(user._Human__age) #this how we access private attributes
print(user) #this will print the magic method __str__ 