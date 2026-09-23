class Human():

    def __init__(self,f,l,a): #passing three parameters inside this magic method 
        self.first_name=f
        self.last_name=l
        self.age=a
    
    def full_name(self):
        print(f"full name:{self.first_name} {self.last_name}") #this how we access attributes inside the class



user=Human("light","yagami",23) 

print(user.last_name) #accesing user last name
user.full_name()
