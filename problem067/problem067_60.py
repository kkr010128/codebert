T,H = 0,0
n = int(input())
for i in range(n):
    S1,S2 = input().split()
    if S1 < S2:
        H += 3
    elif S1 > S2:
        T += 3
    else:
        T += 1
        H += 1
print(T,H)
