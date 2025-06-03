dic = {}
pat = ['S','H','C','D']
rank = [k for k in range(1,14)]

for k in pat:
    for j in rank:
        dic[(k,j)]=0

n = int(raw_input())
for k in range(n):
    p,r = raw_input().split()
    r = int(r)
    dic[(p,r)] +=1

for k in pat:
    for j in rank:
        if dic[(k,j)]==0:
            print '%s %d' % (k,j)