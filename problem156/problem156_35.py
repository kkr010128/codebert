x=int(input())
for a in range(-120,121):
    for b in range(-120,121):
        if x==pow(a,5)-pow(b,5):
            print(a,b)
            exit()