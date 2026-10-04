import random
choices=["rock","paper","scissors"]
print(f"your choices are {choices}")


def game():
    p_score=0
    c_score=0
  
    print("press 1 to exit the game")
    while True:
        inp=input("enter your choice:")
        comp_choice=random.choice(choices)


        if inp=="rock" and comp_choice=="paper":
              c_score+=1
        elif inp=="paper" and comp_choice=="rock":
             p_score+=1
        elif inp=="rock" and comp_choice=="scissors":
             p_score+=1
        elif inp=="scissors" and comp_choice=="rock":
             c_score+=1
        elif inp=="paper" and comp_choice=="scissors":
             c_score+=1
        elif inp=="scissors" and comp_choice=="paper":
             p_score+=1
        elif inp==comp_choice:
             print("tie")
        elif inp=="1":
            if p_score>c_score:
             print("you won")
             
            elif p_score==c_score:
                print("draw")
            else:
                print("you lost")
            print("exiting")
            break
             
        
        else:
             print("choose from the choices provided")




game()

