'''
#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington
State Ferry fare based on age and whether the person has a vehicle. Assume the following rates:
* Adults (19-64): $10 without a vehicle, $20 with a vehicle.
* Seniors (65+): $5 without a vehicle, $15 with a vehicle.
* Children (0-18): Free.
'''

def ferry_fare(age, vehicle):
    if age <= 18:
        return 0
    elif 19 <= age <= 64:
        return 20 if vehicle else 10
    elif age >= 65:
        return 15 if vehicle else 5


print(ferry_fare(30, True))   
print(ferry_fare(30, False))  
print(ferry_fare(70, True))  
