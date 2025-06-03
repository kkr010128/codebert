n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
ans = 0
for i in range(n):
    ans += abs(x[i] - y[i])
print(ans)
ans = 0
for i in range(n):
    ans += (x[i] - y[i])**2
print(ans**(1/2))
ans = 0
for i in range(n):
    ans += (abs(x[i] - y[i]))**3
print(ans**(1/3))
ans = 0
for i in range(n):
    ans = max(ans, abs(x[i] - y[i]))
print(ans)
