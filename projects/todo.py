todo_list=[]



def view():
    print(todo_list)

def add():
    inp_1=input("enter task to be added:")
    todo_list.append(inp_1)
    print(f"updated list: {todo_list}")

def delete():
    inp_2=input("enter index number of task to be deleted:")
    todo_list.pop(inp_2)
    print(f"updated list: {todo_list}")



    

    
 



while True:
    print("1.view 2.add a task  3.delete/complete task  4.exit")
    enter=input("enter your choice:")
    
    if enter=="4":
        print("exiting...")
        break
    elif enter=="1":
        view()
    elif enter=="2":
        add()
    elif enter=="3":
        delete()
    

