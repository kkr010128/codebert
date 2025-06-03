def insertion_sort(a,n,g,cnt):
    for i in range(g,n):
        v = a[i]
        j = i-g
        while j >= 0 and a[j] > v:
            a[j+g] = a[j]
            j -= g
            cnt+=1
        a[j+g] = v
    return a,cnt

def shell_sort(a,n,G):
    cnt=0
    for g in G:
        a,cnt = insertion_sort(a,n,g,cnt)
    return a,cnt

n = int(raw_input())
a = []
for i in range(n):
    a.append(int(raw_input()))

g = 1
G = [g]
while True:
    g = 3*g + 1
    if g > n:
        break
    G.append(g)

G = sorted(G,reverse=True)

a,cnt = shell_sort(a,n,G)
print len(G)
print ' '.join([str(v) for v in G])
print cnt
for v in a:
    print v