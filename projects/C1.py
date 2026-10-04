cart=["apple","peanut butter","protein bar","energy drink"]
final_cart=[]
print("enter y for yes and n for no")
for item in cart:
   dec=input("do you want "+item+ ":")
   if dec=="y":
      final_cart.append(item)
      print("added to cart")

      

   elif dec=="n":
    print('not added to cart') 
   else:
    print("enter y for yes and n for no")
 
print(f"your final cart is {final_cart}")