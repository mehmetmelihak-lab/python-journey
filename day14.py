shopping_list=[]
while True:
    print('Hi.Welcome to the shopping check list.Please enter your desired operation')
    choice=input('\n1: Add\n2: Remove \n3: Show \n4: Clear \n5: Quit \n6 ')
    if choice=='1'or choice.lower()=='add':
        add_=input('Please enter what you would like to add:')
        shopping_list.append(add_)
    elif choice=='2' or choice.lower()=='remove':
        remove_=input('Please enter what you would like to remove:')
            
        if remove_ not in shopping_list:
            print('Hey thats not in our shopping list.Try again please')
            continue
        else:
            shopping_list.remove(remove_)
    elif choice=='3' or choice.lower()=='show':
        result=shopping_list
        print(result)
    elif choice=='4' or choice.lower()=='clear':
        shopping_list.clear()
        
    elif choice=='5' or choice.lower()=='quit':
        break
    else:
        print('Not a good idea')

        
        


        




        
