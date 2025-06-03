n = int(input())
li = list(map(int, input().split()))

s = li[0]

for i in range(1,n):
    s ^= li[i]

ans = []

for i in li:
    tmp = s^i
    ans.append(tmp)
    
print(*ans)