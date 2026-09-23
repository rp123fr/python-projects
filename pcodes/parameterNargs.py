def greeting(name):            #creating a function which on calling will print hello and good morning
    print(f"hello {name}")
    print("good morning")      #suppose we need to print a name with hello 
                               #for it we need to pass a parameter inside the function greeting
                               #suppose we pass a parameter name 
      
greeting("MR.NC")              #we pass a string MR.NC on calling the function which will be stored
                               #in the name parameter created 
                               # the string passed to get stored in the parameter is called argument 
                               
def analyzer(gender,age):      # we can pass multiple parameter in the function 

    print(f"your gender is {gender} and your age is {age} ")

analyzer("male",17) 


def operator(firstname,lastname= "nolan"):
     print(f"your name is {firstname} {lastname}") #creating a default parameter lastname
                                            #note that non-def parameter cant come after def parameter 


operator("christopher") #passing an argument in the parameter firstname