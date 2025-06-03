def freq(my_list):
    count = {} 
    for i in my_list: 
        count[i] = count.get(i, 0) + 1
    return count

n = int(input())
l = list(map(int, input().split()))
s,f = sum(l), freq(l)
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x in f:
        v = f[x]
        if y in f:
            f[y]+=v
            f.pop(x)
        else:
            f[y]=f.pop(x)
        s += (y-x)*v
    print(s)