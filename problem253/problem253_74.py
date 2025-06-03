N, A, B = map(int, input().split())

dif = abs(A-B)
if dif%2 == 0:
    ans = dif//2
else:
    #A left
    t0 = A - 1 + 1
    xa = 0
    xb = B - t0
    dif = abs(xb - xa)
    ans1 = dif//2 + t0
    
    #B left
    t0 = B - 1 + 1
    xa = A - t0
    xb = 0
    dif = abs(xb - xa)
    ans2 = dif//2 + t0
    
    #A right
    t0 = N - A + 1
    xa = N
    xb = B + t0
    dif = abs(xb - xa)
    ans3 = dif//2 + t0
    
    #B right
    t0 = N - B + 1
    xa = A + t0
    xb = N
    dif = abs(xb - xa)
    ans4 = dif//2 + t0
    
    ans = min(ans1, ans2, ans3, ans4)
    
print(ans)