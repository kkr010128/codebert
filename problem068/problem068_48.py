def rev(val, v1, v2):
    for i in range((v2-v1)//2 +1):
        val[v1+i], val[v2-i] = val[v2-i], val[v1+i]
    return val

def rep(val1, val2, v1, v2):
    for i in range(v2-v1):
        val1[v1+i] = val2[i]
    return val1

st = input()
lst = [i for i in st]
q = int(input())
for i in range(q):
    f = list(map(str, input().split()))
    if f[0] == 'print':
        s = ''.join(lst[int(f[1]):int(f[2])+1])
        print(s)
    elif f[0] == 'reverse':
        lst = rev(lst, int(f[1]), int(f[2]))
    elif f[0] == 'replace':
        x = [i for i in f[3]]
        lst = rep(lst, x, int(f[1]), int(f[2])+1)
