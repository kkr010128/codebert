
A, B = map(int, input().split())

for n in range(2000):
    if int(n * 0.08) == A and int(n * 0.1) == B:
        print(n)
        break
else:
    print(-1)
