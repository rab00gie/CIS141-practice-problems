'''
#1. Create a file called gardening_tips.txt and add at least 3 gardening tips to
it. Write a Python script that reads a file gardening_tips.txt and prints
out each tip one by one.
'''

file = open("gardening_tips.txt", "r")
content = file.read()
print(content)
file.close()
