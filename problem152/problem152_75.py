N = int(input())
s = []
for i in range(N):
    s.append(input())
inc = []
dec = []
total = 0
for i in s:
    cn = 0
    mn = 0
    for j in i:
        if j=="(":
            cn+=1
        else:
            cn-=1
        mn = min(cn,mn)
    total += cn
    if cn>=0:
        inc.append([mn,cn])
    else:
        dec.append([mn-cn,-cn])

inc.sort(reverse=True,key=lambda x:x[0])
dec.sort(reverse=True,key=lambda x:x[0])

def check(lis):
    hi = 0
    for i in lis:
        if hi+i[0]<0:
            return False
        else:
            hi+=i[1]
    return True

if check(inc) and check(dec) and total==0:
    print("Yes")
else:
    print("No")
