A, B = map(int, input().split())

ans = -1

for i in range(10000):
    if int((i/100)*8) == A and int((i/100)*10) == B:
        ans = i
        break

print(ans)