import random 
points = 0
hp = 9 
pos = 0
score = 0
for rnd in range(100):
    pos += 1
    if pos == 3 and random.randint(0,1) == 0:
        hp -= 3
        score += .5 
    if pos >= 4:
        score += 2
        score += .5 
        hp -= 6 - random.randint(0,2)
        if random.randint(0,2) == 0:
            score += 1 
    if hp <= 0:
        pos = 0
        hp = 9
        
print(score)


import random 
points = 0
hp = 9 
pos = 0
score = 0
for rnd in range(100):
    pos += 1
    if pos >= 3:
        score += 2
        score += .5 
        hp -= 6
    if hp <= 0:
        pos = 0
        hp = 9
        
print(score)