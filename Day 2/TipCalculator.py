#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.

print("Welcome to the Tip Calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give: 10, 12, or 15? "))
people = int(input("How many people would like to share the bill? "))

tip_as_percentage = tip / 100
total_tip_amout = bill * tip_as_percentage
total_bill = bill + total_tip_amout
bill_per_person = total_bill / people
finaly_bill = round(bill_per_person, 2)

# finaly_bill = "{:2f}".format(bill_per_person)    
# when can also use this when we want to round to two decimal places without the scenario of getting one decimal place.


# FAQ: How to round to 2 decimal places?

# Find the answer in the Q&A here: https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#questions/13315048

print(f"Each person should pay ${finaly_bill}")