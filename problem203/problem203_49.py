A, B = list(map(int, input().split()))
ans = -1
for i in range(1, 1009):
    if int(i*0.08) == A and int(i*0.10) == B:
        ans = i
        break
print(ans)