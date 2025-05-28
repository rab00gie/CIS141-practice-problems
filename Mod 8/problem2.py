'''
#2. Write a Python program that allows users to log their hiking trips. The program
should:
- Use a while loop to repeatedly ask for a hike name and distance in miles
- Save each entry to hiking_log.txt (each hike on a new line)
- When the user presses 0, exit the loop & print the contents of hiking_log.txt
'''

file = open("hiking_log.txt", "a")


while True:
    hike_name = input("Enter hike name (or 0 to quit): ")
    if hike_name == "0":
        break
    distance = input("Enter distance in miles: ")
    file.write(hike_name + " - " + distance + " miles\n")


file.close()


file = open("hiking_log.txt", "r")
content = file.read()
print("\nYour Hiking Log:")
print(content)
file.close()
