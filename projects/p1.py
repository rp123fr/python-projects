expenses=[120,650,45,800,230,550]
expensive=[]
sum=0
for price in expenses:
    sum+=price
    
    if price>500:
        expensive.append(price)

num=len(expensive)

print(f"total expense of this week : {sum}")
print(f"total number of expensive items : {num}")