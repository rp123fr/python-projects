def print_add(num1,num2):
    result=num1+num2
    return result       

sum=print_add(3,6)
print(sum)


# '*' before a parameter makes it dynamic or iterable 
def sum(*num):
    result=0
    for n in num:
        result+=n
    print(result)

sum(4,5,6,7)      #output will be 22                     