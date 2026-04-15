print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))

tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

people = int(input("How many people to split the bill? "))

tip_amount = total_bill * (tip / 100)

total_with_tip = total_bill + tip_amount

pay_each_person = round((total_with_tip) / people, 2)

print(f"Each person should pay: ${pay_each_person}")