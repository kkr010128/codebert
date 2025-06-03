N = int(input())
ans = 0

for i in range(1, N + 1):
    temp = i
    while(temp <= N):
        ans += temp
        temp += i
print(ans)