#while loop do particular set of task until a condition is true 

number=1

while number<=10:     #this code will print even no. from 1 to 10
    if number%2==0:
        print(number)
    number+=1

#break statement is used for stopping a loop when a particular condition is met 

num_1=0

while num_1<=10:
    print(num_1)
    num_1+=1
    if num_1==5:
        break      #this will break the loop when we get 5 


#continue statement is used to skip a iterable item in a loop and does not execute a code below it 



for num in range(10):
    if num==5 or num==8:
        continue           #this code will skip 5 and 8
    print(num)

