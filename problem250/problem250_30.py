X = int(input())
if X <= 2:
    print(2)
    exit()
S = [2]
for i in range(3, 10**6, 2):
    f = True
    for s in S:
        if s > i**(0.5): break
        if i % s == 0:
            f = False
            break
    if f:
        S.append(i)
        if i >= X:
            print(i)
            break
