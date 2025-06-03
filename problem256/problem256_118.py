A, B = map(int, input().split())

for i in range(1, A+1):
    if B*i % A == 0:
        print(B*i)
        break
