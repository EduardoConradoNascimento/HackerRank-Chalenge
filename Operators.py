import sys

meal_cost = float(input("Meal cost:"))
tip_percent = int(input("Tip percent:"))
tax_percent = int(input("Tax:"))

tip_amount = meal_cost * tip_percent / 100
tax_amount = meal_cost * tax_percent / 100

total_amount = round(tip_amount + tax_amount + meal_cost)

print ("The total meal cost is " + str(total_amount) + " dollars.")