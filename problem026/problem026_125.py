N = int(input())
S = list(map(int,input().split()))

def marge(l,r):
    count = 0
    conq = []
    i = 0
    j = 0
    k = len(l) + len(r)
    l.append(float('inf'))
    r.append(float('inf'))
    for o in range(k):
        if l[i] <= r[j]:
            conq.append(l[i])
            i += 1
        else:
            conq.append(r[j])
            j += 1
        count += 1
    return conq,count
           
def margeSort(s):
    n = len(s)
    if n == 1:
        return s,0
    else:
        L, cnt_L = margeSort(s[:n//2])
        R,cnt_R = margeSort(s[n//2:])
        s,cnt = marge(L,R)         
    return s,cnt+cnt_R+cnt_L
S,count = margeSort(S)
print(*S)
print(count)
