N = int(input())
P = list(map(int,input().split()))
count = 0
minlist = []

for i,p in enumerate(P) :
    if i == 0 :
        minlist.append(p)
        continue

    if p < minlist[i-1] :
        minlist.append(p)
    else:
        minlist.append(minlist[i-1])
    
for i,p in enumerate(P) :
    pj_min = minlist[i]
    if p <= pj_min :
        count += 1
    
print(count)