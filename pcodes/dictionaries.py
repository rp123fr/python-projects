#dictionaries is a set of key-value pair 
{"z":5} #here z is key and 5 is the value

#there is another method of creating dictionaries using the dict() function 

dict_1=dict(name="mr.nc",hobby="coding")
#print(dict_1)

#to access data in a dictionaries you need to call the key 
#print(dict_1["name"])

#we can change the value in a key 
#dict_1["name"]="ghost"
#print(dict_1["name"])

#we can add a data in a dictionarie
dict_1["fav sport"]="football"
dict_1["coding style"]="consistent"
#print(dict_1)

#to delete data we use del function 

#del dict_1["name"]
#print(dict_1)


#for x in dict_1:
   # print(x)      #this code will only print the key of the dictionarie

#for key in dict_1:
#    print(key,dict_1[key]) #this code will print key with its value

for y in dict_1.items():
    print(y)                #this code will print key-value pair in a tuple