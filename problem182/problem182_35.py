n,k,c = map(int,raw_input().split())
s = raw_input()
most = [0]*(n+1)
i = n
days = 0
while i > 0:
    if s[i-1] == 'o':
        days += 1
        for j in xrange(min(max(1,c),i-1)):
            #print days
            #print i,j,1,days
            most[i-j-1] = days
        i -= (c+1)
    else:
        i -= 1
        if i<n:
            most[i] = most[i+1]

remain = k
i = 1
while i<=n:
    if s[i-1] == 'o':
        if most[i] < remain:
            print i
        remain -= 1
        i += c+1
    else:
        i += 1