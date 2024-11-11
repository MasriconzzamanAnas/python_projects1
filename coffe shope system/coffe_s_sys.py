def coffee_shop():
    
    menu= {
        "Coffee": 12.99,
        "Tea": 10,
        "Pizza": 80,
        "Pasta": 36.99,
        "Burger": 45,
        "Sandwich": 20
    }

    #! Great the coustomar 
    print("Welcome to the python coffee shop!\n")
    print("What you want?")
    print("Coffee")
    print("Tea")
    print("Pizza")
    print("Pasta")
    print("Burger")
    print("Sandwich")

    items = []
    price = 0
    
    while True:
        choise = input("What you want: ").capitalize()
        try:
            if choise in menu:
                items.append(choise)
                price += menu[choise]
                print(f"Your item {items} has been added to your order")

            else:
                print("Invalid option. Please choose from the menu.")          
        except Exception as e:
            print(e)
        #! Asking the customer if they want to add anything else
        another_order = input("Do you want to add another item? (yes/no): ")
        if another_order.lower() != 'yes':
            break  
    print(f"\nYour order is: {items}")
    print(f"Total price: ${price:.2f}")
    
coffee_shop()    
  

    





