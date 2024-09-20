def calculator():
    while True:
        print('\nSelect operation: ')
        print('1. Add')
        print('2. Subtract')
        print('3. Multiply')
        print('4. Divide')
        print('5. Modulus')
        print('6. Exit ')
        opera = int(input('Enter choice (1/2/3/4/5/6):'))

        if opera == 6:
            print("Exiting the calculator. Goodbye!")
            break

        if opera in [1,2,3,4,5]:
            try:
                nu1 = float(input("Enter first number: "))
                nu2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numerical values.")
                continue

        if opera == 1:
            print(f"Result {nu1} + {nu2} = {nu1 + nu2}")
        elif opera == 2:
            print(f"Result: {nu1} - {nu2} = {nu1 - nu2}")
        elif opera == 3:
            print(f"Result {nu1} * {nu2} = {nu1 * nu2}")
        elif opera == 4:
            if nu1 !=0 and nu2 != 0:
                print(f"Result: {nu1} / {nu2} = {nu1 / nu2}")
            else:
                print("Error: Cannot divide by zero.")
        elif opera == 5:
            if nu2 != 0 and nu1 !=0:
                print(f"Result: {nu1} % {nu2} = {nu1 % nu2}")
            else:
                print("Error: Cannot Modulus by zero.")
        else:
            print("Invalid choice! Please select a valid operation.")


calculator()

