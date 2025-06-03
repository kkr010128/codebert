n = int(input())
a = [int(x) for x in input().split()]
 
m = [0]*(max(a)+1)
lm = len(m)
cnt = 0
 
for i in a:
    j = 1
    while i*j < lm:
        m[i*j] += 1
        j += 1
for i in a:
    if m[i] == 1:
        cnt += 1
print(cnt)