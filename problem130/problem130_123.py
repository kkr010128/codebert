import random

name = str(input())
a = len(name)

if  3<= a <= 20:
    b = random.randint(0,a-3) 
    
    ada_1 = name[b]
    ada_2 = name[b+1]
    ada_3 = name[b+2]
    
    print(ada_1+ada_2+ada_3)
else:
    None