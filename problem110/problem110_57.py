import copy

h, w, k = map(int, input().split())
clist0 = []
result = 0
for i0 in range(h):
    c = list(input())
    clist0.append(c)
for i in range(2**h):
    for j in range(2**w):
        clist = copy.deepcopy(clist0)
        for hi in range(h):
            #print(i, hi)
            if((i & 2**hi) == 2**hi):
                #print(i, hi)
                for j2 in range(w):
                    clist[hi][j2] = "1"
        for wi in range(w):
            if((j & 2**wi) == 2**wi):
                for i2 in range(h):
                    clist[i2][wi] = "1"
        temp = 0
        #print(clist)
        for ci in clist:
            temp += ci.count("#")
        if(temp == k):
            result +=1
print(result)