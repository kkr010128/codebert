def update(i,x):
    i += d-1
    bit = ord(x)-97
    seg[i] = 0 | (1<<bit)
    while i > 0:
        i = (i-1)//2
        seg[i] = seg[i*2+1]|seg[i*2+2]
def find(a,b,k,l,r):
    if r <= a or b <= l:
        return 0
    if a <= l and r <= b:
        return seg[k]
    c1 = find(a,b,2*k+1,l,(l+r)//2)
    c2 = find(a,b,2*k+2,(l+r)//2,r)
    return c1|c2
n = int(input())
s = input()
q = int(input())
d = 1
while d < n:
    d *= 2
seg = [0]*(2*d-1)
for i in range(n):
    update(i,s[i])
for i in range(q):
    type,a,b = input().split()
    if type == "1":
        update(int(a)-1,b)
    else:
        part = find(int(a)-1,int(b),0,0,d)
        print(bin(part).count("1"))
