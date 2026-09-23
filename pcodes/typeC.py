#input function converts all data type into string 
#num_1=input("enter a number:")  #this code will throw error since num_1 get stored as string
#additon=num_1+5
#print(additon)
#for running this code we need to convert num_1 into an integer 

num_1=input("enter a number:")
#for converting num_1 into an inger we use int() function
addition=int(num_1)+9
print(addition)
#output will be the sum of num_1 and 9

str_1="good"
print(type(str_1)) #knowing the data type of str_1
bool_1=bool(str_1) #converting the data type of str_1 into a boolean expression
print(bool_1)  

#int()
#str()
#bool()
#float()

float_1=5.09
int_1=int(float_1) #converting a float variable inta an integer and storing it into int_1
print(int_1)
