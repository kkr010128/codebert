X=int(input())
def check():
    for a in range(-200,200):
        for b in range(-200,200):
            if a**5-b**5==X:
                print(a,b)
                return 0
check()