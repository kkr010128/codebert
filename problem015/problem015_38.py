n = int(input())
s = [ i for i in input().split()]
cnt = 0
for i in range(n-1):
    minj = i
    for j in range(i+1,n):
        if int(s[j]) < int(s[minj]):
            minj = j
    if i != minj:
        cnt += 1
        s[i],s[minj] = s[minj],s[i]
print(' '.join(s))
print(cnt)

