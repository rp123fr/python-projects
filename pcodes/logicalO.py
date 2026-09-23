# logical operators are and,or,not
# it is used for checking 2 conditions at a time 

gender=input("enter 'm' for male and 'f' for female:")
marks_1=float(input("enter your class 10th marks:"))
marks_2=float(input("enter your class 12th marks:"))


if marks_1>=75 and marks_2>=75: #using and operator to combine two conditions together
    print("Eligible")

    if gender=="m":
     print("40% discount")
     

    elif gender=="f":
     print("60% discount")


    else:
       print("enter m for male and f for female! ")    

else:
    print("Not Eligible")

