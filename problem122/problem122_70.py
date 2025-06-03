n = int(input())
a = list(map(int,input().split()))
q = int(input())

table = {}
sum = 0


for i in range(n):
    sum += a[i]
    if a[i] not in table.keys():
        table[a[i]] = 1
    else:
        table[a[i]] += 1
for i in range(q):
    b,c = map(int,input().split())
    if b in table.keys():
        sum -= b * table[b]
        sum += c * table[b]
        
        if c not in table.keys():
            table[c] = table[b]
        else:
            table[c] += table[b]
        table[b] = 0    
    print(sum)    
