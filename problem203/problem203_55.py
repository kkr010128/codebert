A, B = map(int, input().split())

N = 1000
p1 = 0.08
p2 = 0.1

for i in range(1, N + 1):
    if int(i * p1) == A and int(i * p2) == B:
        print(i)
        exit()

print("-1")