#lamda function is a tool used for short operating functions
#it has no name 

#syntax of lamda function:  lamda parameter:expression 
# we can pass endless parameter in lambda function but expression can be only one line

multiply=lambda a,b:a*b
result=multiply(4,5)
print(result)

#tuple is created by () brackets 
#students_mark=[("james",95),("einstein",98),("newton",100),("bohr",96)]
#names=[]
#for x in students_mark:
#    names.append(x[0])       #adding 1st element of tuple in name list 
#print(names)

#the same thing done in the above code can be done by map function
#syntax of map function: map(function,iterable)

students_mark=[("james",95),("einstein",98),("newton",100),("bohr",96)]

names=list(map(lambda x:x[0],students_mark)) #creating a lambda function that will return 1st element of tuple
print(names)

