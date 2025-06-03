A,B,C,D = map(int,input().split())
while True:
    C -= B
    A -= D
    if C <= 0:
        print("Yes")
        exit()
    elif A <= 0:
        print("No")
        exit()