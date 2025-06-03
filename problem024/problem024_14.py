def check(p):
    global k, wlist   
    loadage = 0
    num = 1
    
    for w in wlist:
        loadage += w
        if loadage > p:
            num += 1
            if num > k:
                return False
            loadage = w
    return True

n, k = map(int, input().split())
wlist = []

for _ in range(n):
    wlist.append(int(input()))
    
maxw = max(wlist)
sumw = sum(wlist)
p = 0

while maxw < sumw:
    p = (maxw + sumw) // 2
    if check(p):
        sumw = p
    else:
        maxw = p = p+1
        
print(p)
