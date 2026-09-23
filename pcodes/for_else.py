#else statement regarding a for loop will execute if the for loop ends normally and does not break 

for number in range(3):
    num=int(input("enter an odd number:"))
    if num%2==0:
        print("you loose")
        break
else:
    print("you won")
