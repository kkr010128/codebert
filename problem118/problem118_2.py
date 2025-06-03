N = int(input())

#1 is dividable by all
#-> sum = 1 + 2 + .. + N = (N+1)*N//2
ans = (N+1)*N//2
for num in range(2, N+1):
    for tt in range(N//num+1):
        ans += num*tt

print(ans)
