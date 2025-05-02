'''#5. A store charges $5 for shipping on any order under $50. 
If the order amount is $50 or more, shipping is free. 
Ask the user for the order total and print the total cost, 
including shipping.'''

#Ask user for the order total
order_total = float(input("Enter your order total: $"))

#Shipping cost 
if order_total < 50:
    shipping = 5
else:
    shipping = 0

#total cost
total_cost = order_total + shipping


#Print te total including shipping 
print(f"Your total cost including shipping is: ${total_cost:.2f}")
