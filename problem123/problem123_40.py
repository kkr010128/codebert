N = int(input())
A = list(map(int, input().split()))

temp = 0
for a in A:
    temp ^= a
    
ans =[]
for a in A:
    ans.append(temp^a)
print(*ans)