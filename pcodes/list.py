#list is a collection of iterable objects 

anime=["naruto","bleach","one_piece","JJK"]   
for y in anime: 
    print(y)      #accesing elements in anime

marks=[[87,94,85],[89,98,86],[97,91,92]]  #list can be nested 

ult_list= anime + marks  #list can be combined
print(ult_list)


list_1=[]
for x in range(1,22):
    list_1.append(x)    #append() function is used to add items in a list 
print(list_1)

text_1="my name is mr.nc"
list_2=[]
for char in text_1:
    list_2.append(char)
print(list_2)
print(len(list_2))       #this line will print the length of list_2


list=["up","down","left","right"]
slice_list=list[0:2] #slicing list from index 0 to 2 
print(slice_list)


name=["cole","joe","jude","harry"]
a,b,c,d=name  #this will unpack the list and store the elements indivdually in the variables a,b,c
print(f"{a} {b} {c} {d}")
new_list=["michael","kylian","dembele",1,2,3,4]
x,y,z,*list3=new_list # * before list3 will make it a list and store 1,2,3,4 in it 
print(f"{x} {y} {z} {list3}")

language=["java","c++","javascript"]
language.append("python")   #append function adds element at the end of list
print(language)             #append function changes the original  function

#for adding elements in between of list we use insert function

language.insert(1,"html")  #this will add html and displace c++ to 2 place
print(language)

#for removing elements out of list we use pop function
language.pop(3)   # this will remove the element indexed 3 that is javascript
print(language)

# there is remove function that uses element character instead of its index
language.remove("java")
print(language)


numbers=[89,93,98,12,56,61]
numbers.sort()  #this will sort numbers in the list in ascending order
print(numbers)
numbers.sort(reverse=True) #this will sort numbers in descending order
print(numbers)