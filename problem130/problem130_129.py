import random

def name(x):
    if len(x) > 20:
        return name()
    if len(x) < 3:
        return name()
    if x.isupper() == True:
        return name()
    if x.isalpha() == False:
        return name()
    else:
        l = list(x)
        w = random.randint(0, len(x) - 3)
        y = l[w]
        z = l.index(y)
        print(y + l[z+1] + l[z+2])
        
S=input()
name(S)