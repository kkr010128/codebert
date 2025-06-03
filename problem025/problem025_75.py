def ans(n, AA, x):
    tmp = n + AA[0]
    if len(AA) == 1:
        try: x[tmp] = 1
        except: pass
    else:
        ans(n, AA[1:], x)
        try:
            x[tmp] = 1
            ans(tmp, AA[1:],x)
        except:
            pass
    return
 
n = raw_input()
A = map(int, raw_input().split())
q = raw_input()
M = map(int, raw_input().split())
 
x = [0 for i in range(max(M)+1)]
ans(0, A, x)
 
for e in M:
    if x[e] == 1:
        print 'yes'
    else:
        print 'no'