import sys
input = sys.stdin.buffer.readline

n = int(input())
l = list(map(int,input().split()))
l.sort()
mx = l[-1]+l[-2]

length = [0]*(mx+1)
for i in range(n):
    for j in range(i+1,n):
        length[l[i]+l[j]] -= 1
        length[l[j]-l[i]+1] += 1

for i in range(1,mx+1):
    length[i] += length[i-1]

minus = [0]*n
for i in range(n):
    a = i
    for j in range(i+1,n):
        if l[i]*2 - 1 >= l[j]:
            a += 1
    minus[i] = a
#print(length)
#print(minus)
ans = 0
for i in range(n):
    ans += length[l[i]] - minus[i]


print(ans//3)