A, B, C, D=map(int,input().split())

while C or A >= 0:
    C -= B
    A -= D
    if C <= 0:
        print("Yes")
        break
    if A <= 0:
        print("No")
        break