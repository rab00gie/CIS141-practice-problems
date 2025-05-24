'''
#5. Write a function called level_up(experience) that takes a player's experience
points and returns their new level based on these rules:
* 0-99 XP → Level 1
* 100-199 XP → Level 2
* 200+ XP → Level 3
'''

def level_up(experience):
    if experience < 100:
        return "Level 1"
    elif experience < 200:
        return "Level 2"
    else:
        return "Level 3"


print(level_up(0))       
print(level_up(99))      
print(level_up(100))     
print(level_up(150))     
print(level_up(200))     
print(level_up(300))   
