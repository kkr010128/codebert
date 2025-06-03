def rvrs(base, start, end):
    r = base[int(start):int(end) + 1][::-1]
    return base[:int(start)] + r + base[int(end) + 1:]
def rplc(base, start, end, string):
    return base[:int(start)] + string + base[int(end) + 1:]

ans = input()
q = int(input())
for _ in range(q):
    ORD = list(input().split())
    if ORD[0] == 'print':
        print(ans[int(ORD[1]):int(ORD[2])+1])
    elif ORD[0] == 'reverse':
        ans = rvrs(ans, int(ORD[1]), int(ORD[2]))
    elif ORD[0] == 'replace':
        ans = rplc(ans, int(ORD[1]), int(ORD[2]), ORD[3])
