n = int(input())
arr = [int(x) for x in input().split()]
d = {}
for ele in arr:
    if ele in d:
        d[ele] += 1
    else:
        d[ele] = 1

q = int(input())
s = sum(arr)
while(q>0):
    a,b = [int(x) for x in input().split()]
    if a in d:
        x = d[a]
        s -= int(x*a)
        s += int(x*b)
        d.pop(a)
        if b in d:
            d[b]+=x
        else:
            d[b] = x
    print(s)

    q-=1