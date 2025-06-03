A, B = map(int, input().split())
for p in range(1, 100001):
    if int(p*0.08) == A and int(p*0.1) == B:
        print(p)
        break
    if p == 100000:
        print(-1)