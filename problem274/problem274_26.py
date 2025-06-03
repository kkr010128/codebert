n,m = [int(i) for i in input().split()]
s = input()
p = n
q = []

while p!=0:
    frag = True
    for i in range(max(p-m,0),p):
        if s[i]=='0':
            q.append(p-i)
            p=i
            frag = False
            break
    if frag:
        q=[]
        print(-1)
        break
        
for i in reversed(q):
    print(i)
