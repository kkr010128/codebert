import copy
import itertools

h, w, k = map(int, input().split())
#s= list(input())

s = []
min = 100000
for i in range(h):
    s.append( [int(s) for s in list(input())])
    #s.append([1]*w)

dbg_cnt = 0
l = list(range(h-1))
for i in range(h):
    p = list(itertools.combinations(l, i))
    for j in p:
        tmp = list(j)
        tmps = []
        q = 0
        tmps.append([])
        #print(dbg_cnt)
        #dbg_cnt += 1
        for r in range(h):
            tmps[q].append(copy.copy(s[r]))
            if(q < len(tmp) and r==tmp[q]):
                tmps.append([])
                q += 1
        #print(tmps)
        count = i
        sums = [0] * len(tmps)
        precut = 1
        exitflg = 0
        for r in range(w): #550000
            for q in range(len(tmps)):
                for t in tmps[q]:
                    sums[q] += t[r] #5500000
            cutflg = 0
            for q in range(len(tmps)):
                if sums[q] > k : #5500000
                    cutflg = 1
            if cutflg == 1:
                #print('cut')
                count += 1
                sums = [0] * len(tmps)
                for q in range(len(tmps)):
                    for t in tmps[q]:
                        sums[q] += t[r] #5500000
            for q in range(len(tmps)): #5500000
                if sums[q] > k :
                    exitflg = 1
                    #print('exit')
        #print(exitflg)
        if exitflg == 0:
            if min > count:
                min = count
print(min)