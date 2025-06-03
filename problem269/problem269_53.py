T = [int(t) for t in input().split()]
A = [int(t) for t in input().split()]
B = [int(t) for t in input().split()]

d1 = T[0]*(A[0]-B[0])
d2 = d1 + T[1]*(A[1]-B[1])

if d2 == 0:
    ans = "infinity"
elif d1 > 0 and d2 > 0:
    ans = 0
elif d1 < 0 and d2 < 0:
    ans = 0
else:
    d1 = abs(d1)
    d2 = abs(d2)
    ans = d1 // d2 * 2
    if d1%d2 != 0:
        ans += 1 
    
    
print(ans)