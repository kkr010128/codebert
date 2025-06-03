import copy,collections
N = int(input())
s = ['a']
for i in range(2,N+1):

    tmp = copy.copy(s)
    tmp2 = []
    for tm in tmp:
        tc = collections.Counter(tm)
        lc = len(tc.values())
        for j in range(1,lc+2):
            tmp2.append(tm+chr(96+j))
    s = copy.copy(tmp2)
for sa in s:
    print(sa)
