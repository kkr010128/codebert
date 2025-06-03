n = int(input())
s = [ i for i in input().split()]
flag = True
cnt = 0
while flag:
    flag = False
    for i in range(n-1):
        if int(s[i]) > int(s[i+1]):
            s[i],s[i+1] = s[i+1],s[i]
            flag = True
            cnt += 1
print(' '.join(s))
print(cnt)

