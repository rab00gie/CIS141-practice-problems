'''# 3. Create a program that prompts for the side lengths of a triangle and computes the area using Heron's formula.
(https://en.wikipedia.org/wiki/Heron%27s_formula)'''

# Get the side lengths from the user
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))


s = (a + b + c) / 2

# Calculate area using Heron's formula
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

# Show the result
print("The area of the triangle is:", area)

