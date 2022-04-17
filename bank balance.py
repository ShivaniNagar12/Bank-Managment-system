print("Welcome to the bank")
restart = ['Y']
chances = 3
balance = 70.67
while chances>=3:
    pin = int(input("Enter your 4 digit pin here"))
    if pin == (1234):
           print("You entered correct pin")
           while restart not in ('n', 'no', 'NO', 'N'):
               print("press 1 for check bank balance")
               print("press 2 to make withdraw")
               print("press 3 to pay")
               print("press 4 to return card")
               option = int(input("what would you like to do???"))
               if option ==1:
                   print("your acc balance is:", balance)
                   restart = input("would you like to go back?")
                   if restart in ('n', 'no','NO', 'N'):
                       print("THANK YOU")
                       break
               elif option == 2:
                   print("Y")
                   withdraw = float(input("enter the amount of withdraw"))
                   if withdraw in [10,20,40,60]:
                       balance = balance-withdraw
                       print("your current balance is:", balance)
                       restart = input("would you like to go back?")
                       if restart in ("n", "no", "NO", "N"):
                           print("THANK YOU")
                           break
                   elif withdraw !=[10,20,40,60]:
                       print("Invalid Amount, Reentered the valid amount")
                       restart("Y")
                   elif withdraw == 1:
                      withdraw =float(input("Enter desired amount:"))

               elif option ==3:
                   print("Y")
                   pay = float(input("How much would you like to pay in ??"))
                   balance = balance+pay
                   print("your current balance is:", balance)
                   restart = input("would you like to go back?")
                   if restart in ("n", "no", "NO", "N"):
                       print("THANK YOU")
                       break
               elif option == 4:
                   print("Take a litle pateince while your card is returned!!")
                   print("Thank you so much for your service")
               else:
                   print("Please entered correct pin")
                   restart("Y")
    elif pin!= ('1234') :
        print("enetr correct pin")
        chances = chances-1
        if chances==0:
            print("No more chances")
            break




