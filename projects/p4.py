balance=1000

while True:
   print("option menu: 1.check balance 2.deposit money 3.withdraw money 4.exit")
   
   option=int(input("choose a option:"))

   if option==1:
      print(balance)
      
   elif option==2:
      deposit=int(input("amount of money getting deposit:"))
      balance+=deposit
      print(f"balance remaining: {balance}")
      
   elif option==3:
      withdraw=int(input("amount of money getting withdraw:"))
      if withdraw>balance:
         print("not enough balance!error")
         
      else:
       balance-=withdraw
       print(f"balance remaining : {balance}")
       
   elif option==4:
      print("thank you!")
      break
   else:
      print("please choose an option")

   