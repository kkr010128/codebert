def step_sum(n):

    return (n*(n+1))//2

n = int(input())
table = [0]*n
ans = 0
for i in range(1, n+1):
    ans += i*step_sum(n//i)
print(ans)