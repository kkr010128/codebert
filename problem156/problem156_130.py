x = int(input())
def f(a,b):
    return a**5-b**5

for a in range(-120,120):
    for b in range(-120,120):
        if f(a,b)==x:
            print(a,b)
            exit()