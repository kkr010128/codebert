n,m = map(int,input().split())
ac = [0]*n
wa = [0]*n
count_ac = 0
count_wa = 0

for i in range(m):
    p,s = input().split()
    p = int(p)
    if ac[p-1]:
        continue
    
    if s == "WA":
        wa[p-1] += 1
    else:
        ac[p-1] = True
        count_ac += 1
        count_wa += wa[p-1]
        
print(count_ac,count_wa)