#nested loop means using a loop inside a loop 

for x in range(1,6):      #this code will print table of 1 to 5
    print(f"table of {x}")
    for y in range (1,11):
        print(f"{x}x{y}={x*y}")
    print("------------------")

#*
#**
#***
#****
#*****

for z in range(5):
    print("*",end="")  #this code will print all the stars in the same line



for p in range(1,6):           #this code will print a pattern of stars
    for q in range(1,p+1):
        print("*",end="")
    print("")


num_1=1            #this code will also print a pattern same as the above code
while num_1<=5:
    for a in range(1,num_1+1):  
        print("*",end="")
    print("")
    num_1+=1


line=1
while line<=5:     #this code will also print a pattern same as the above code
    star=1
    while star<=line:
        print("*",end="")
        star+=1
    print("")
    line+=1



for a in range(1,6):   #this code will also print a pattern same as the above code
    b=1
    while b<=a:
        print("*",end="")
        b+=1
    print("")

        

 
