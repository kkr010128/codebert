n = int(input())
A = list(map(int,input().split()))
data = [0]*3
ans = 1
mod = pow(10,9)+7
for i in A:
    ans *= data.count(i)
    ans %= mod
    if ans == 0:
        break
    data[data.index(i)] += 1
print(ans)