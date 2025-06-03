import random
name = list(input())
i = random.randint(0,len(name)-3)
print(name[i],end="")
print(name[i+1],end="")
print(name[i+2])