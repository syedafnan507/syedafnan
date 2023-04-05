print("welcom to the tip calculator")
z = float(input("what is the total bill ?"))
x = int(input("what percentage tip would you like to give ? 10 , 12 or 15 ?"))
y = int(input("how many people to split the bill:"))
bill_with_tip = x/100 * z + z 
print(f"bill wit tip is  {bill_with_tip}")
bill_per_person = bill_with_tip/y
print(f"each person should pay rupees {(round(bill_per_person, 2))}")