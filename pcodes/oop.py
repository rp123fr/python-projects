#class is a blueprint of object
#for eg bmw is an object under class car
#for eg valorant is an object under class games 

#functions created inside a class are called methods


#making a class named human
class Human():
                          #magic method get called during certain events
    def __init__(self):   #this method is called magic method because it will get call automatically if the class is called
        print("human created")
        self.name="mr.nc"  #this how we create a class variable called attributes
        self.age="**"

    def work(self):          #we need to pass a parameter called self in methods 
        print("working...")     #creating a method inside the class human which will make the human work
    
    def code(self):
        print("coding...")

me=Human()  #calling the method from the class  
me.work()
me.code()         

#print(me.name)  #this is how we access the attribute 

me.name="L"     #this how we can change the attribute of an object   
print(me.name)  #we can also set the attributes of an object by passing parameter in the magic method    


