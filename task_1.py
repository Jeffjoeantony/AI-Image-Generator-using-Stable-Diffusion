print("Welcome to ABC Restaurant")
a = input("!! Press enter key to proceed !!")

c_name = input("Please enter your name: ")
c_phone = int(input("Please enter your phone number: "))
c_details = {c_name,c_phone}

menu = {
    "Veg Fried Rice": 100.00,
    "Non-veg Fried Rice": 120.00,
}

print()
print("     --------M.E.N.U--------     ")
print("  Items                    Price")
print("1.Veg Fried Rice           100.00")
print("2.Non-veg Fried Rice       120.00")

print()

print("Choose any 2 items")
itm1 = input("Enter item 1: ")
qty1 = int(input("Quantity: "))

item1_total = menu[itm1] * qty1

itm2 = input("Enter item 2: ")
qty2 = int(input("Quantity: "))

item2_total = menu[itm2] * qty2

total_bill=item1_total+item2_total

print("-----------------")
print("     BILL        ")
print("Customer: ",c_details)
print(f"{itm1} * {qty1} = {item1_total}")
print(f"{itm2} * {qty2} = {item2_total}")
print("Total:",total_bill)

