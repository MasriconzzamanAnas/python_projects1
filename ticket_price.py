def calculate_ticket_price(age, show_time):
    # বয়স অনুযায়ী টিকেটের দাম নির্ধারণ
    if age <= 10:
        price = 300
    elif 11 <= age <= 25:
        price = 500
    elif 26 <= age <= 60:
        price = 800
    elif age > 60:
        price = 400
    else:
        return "Invalid input. Age must be a positive integer."

    # শোয়ের সময় অনুযায়ী ছাড় প্রযোজ্য
    if 0 <= show_time <= 2359 and isinstance(show_time, int):
        if show_time < 1700:  # বিকাল ৫টার আগে হলে ১০% ছাড়
            discount = price * 0.10
        else:
            discount = 0
    else:
        return "Invalid input. Please provide the showtime in the correct format."
    
    discounted_price = price - discount
    return f"Ticket price: {price} BDT\nDiscount: {discount:.2f} BDT\nDiscounted price: {discounted_price:.2f} BDT"

# ইনপুট নেয়া হচ্ছে
try:
    age = int(input("Age: "))
    show_time = int(input("Showtime (HHMM): "))
    
    # বয়স এবং শোয়ের সময়ের বৈধতা যাচাই
    if age > 0:
        result = calculate_ticket_price(age, show_time)
        print(result)
    else:
        print("Invalid input. Age must be a positive integer.")
except ValueError:
    print("Invalid input. Please provide a valid positive integer for age and a valid time for showtime.")


#? calculate ticket price in nested if condition