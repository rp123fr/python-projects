marks=input("enter your marks:") #taking input from the user 
float_m= float(marks)  #converting the input into float data type since input is always store as string

if float_m>=90:
    print("Grade: A ")        #using conditional statements 

elif 75<float_m<90  :         #else if is syntaxed as elif
    print("Grade: B")                             

elif 60<float_m<75:
    print("Grade: C")

else:
    print("Grade: D")

    




