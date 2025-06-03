N  = int(input())
S = input()
P = 0
count = 0
for j in range(1000):
    V = str(P).zfill(3)
    p1 = False
    p2 = False
    for i in range(N):
        if S[i] == V[0] and not p1:
            p1 = True
            continue
        if S[i] == V[1] and p1 and not p2:
            p2 = True
            continue
        if S[i] == V[2] and p2:
            count += 1
            break
    P += 1
print (count)