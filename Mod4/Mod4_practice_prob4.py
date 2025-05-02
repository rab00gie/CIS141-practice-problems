'''#4. A theater wants to enforce age restrictions for movie tickets.
Ask the user for their age, 
and tell them whether they can see G (appropriate for under 13), 
PG-13 (appropriate for 13 to 17), or 
R (appropriate for over 18) rated movies.'''

# Age of the user
age = int(input("Enter your age:"))


#Check movie rating 
if age < 13:
    print("You can watch G-rated movies.")
elif age >= 13 and age < 18:
    print( " You can watch G and PG-13 rated movies.")
else:    
    print("You can watch G, PG-13, and R-rated movies.")
