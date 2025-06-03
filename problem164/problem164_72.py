A, B, C, D = map(int, input().split())
ctr = 0

while True:
    if C <= 0:
        print("Yes")
        break
    if A <= 0:
        print("No")
        break
    if ctr % 2 == 0:
        C -= B
    else:
        A -= D
    ctr += 1
