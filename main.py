def deposit():
    while True:
        amount = input("What would you like to deposut? £")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter a positive number.")