n = int(input())
seq = list(map(int, input().split()))
q = int(input())
mlist = list(map(int, input().split()))
mins = min(seq)
sums = 0
for a in seq:
    sums += a

def check(i, m):
    global mins
    if m == 0:
        return True
    elif i >= n or mins > m:
        return False
    res = check(i+1, m) or check(i+1, m - seq[i])
    return res

for m in mlist:
    if (mins > m or sums < m):
        print('no')
    elif(check(0,m)):
        print('yes')
    else:
        print('no')
