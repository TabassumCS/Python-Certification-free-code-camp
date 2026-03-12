base_price = 15
age = 21
seat_type = "Gold"
show_time ="Evening"

#check if user is eligible to book a movie ticket
if age>17:
    print("User is eligible to book a ticket")

#check if user is elgible for evening shows
if age>=21:
    print("User is eligible for Evening shows")
else:
    print("User is not eligible for Evening shows")

is_member = False
is_weekend = False

discount = 0
#The membership discount should only apply to members if their age is greater than or equal to 21.
if is_member and age>=21:
    discount = 3
    print("User qualifies for membership discount")
else:
    print("User does not qualify for membership discount")

print("Discount:", discount)

#if its weekend pr show is in the evening apply extra charge
extra_charges = 0

if is_weekend or show_time == "Evening":
    extra_charges = 2
    print("Extra charges will be applied")
else:
    print("No extra charges will be applied")

print("Extra charges:", extra_charges)

#check if user satisfies the condition to book a movie ticket
if age>=21 or age>=18 and (show_time != "Evening" or is_member) :
    print("Ticket booking condition satisfied")
    service_charges = 0
    if seat_type == "Premium":
        service_charges = 5
    elif seat_type == "Gold":
        service_charges = 3
    else:
        service_charges = 1
        print("Service charges:", service_charges)
    #calculate the final price by adding extra charges and service charges to the base price
    final_price = service_charges + extra_charges +base_price - discount
    print("Final price of ticket:",final_price)
else:
    print("Ticket booking failed due to restrictions")

