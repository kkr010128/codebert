x = int(input())
for a in range(-120,121):
    for b in range(-120,121):
        if a**5 - b**5 == x:
            print(a,b)
            exit(0)