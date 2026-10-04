secret_password="python123"
attempt=0
while True:
    password=input("enter the password: ")
    
    if password==secret_password:
        print("Access Granted!")
        break
    else:
        
        attempt+=1
        if attempt==3:
            print("Account Locked!")
            break
        print("Access denied .Try again")
