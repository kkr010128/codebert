n = int(input())
lis = list(map(int,input().split()))
num = [0 for i in range(n)]
ans = 1
for nu in lis:
    if nu == 0:
        ans *= (3-num[0])
    else:
        ans *= (num[nu-1]-num[nu])
    ans %= 10 ** 9 + 7
    num[nu] += 1
print(ans)