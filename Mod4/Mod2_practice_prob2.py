'''#2. The headlights of a car should only automatically
turn onwhen the daylight outside is below a certain threshold.
If a sensor threshold is below the number 8, 
print "Headlights On"; otherwise, print "Headlights Off".'''

#Ask user for the light level 

light_level = int(input("Enter the current light level (0-10):"))

#Check if the light level is below the threshold
if light_level < 8:
    print("Headlights On")
else:
    print("Headlights off")  
