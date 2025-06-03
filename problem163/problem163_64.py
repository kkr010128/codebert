val = input().split()

sheep = int(val[0])
wolf = int(val[1])

if (wolf - sheep) >= 0:
    print("unsafe")
else:  
    print("safe")