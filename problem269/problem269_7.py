def solve(t1, t2, a1, a2, b1, b2):
    if a1 * t1 + a2 * t2 == b1 * t1 + b2 * t2:
        return 'infinity'
    if a1 * t1 + a2 * t2 > b1 * t1 + b2 * t2:
        a1, a2, b1, b2 = b1, b2, a1, a2
    
    at = a1 * t1 + a2 * t2
    bt = b1 * t1 + b2 * t2
        
    ans = 0
    dg = bt - at
    if a1 > b1:
        ans += ((a1 - b1) * t1 - 1) // dg
        ans += (a1 - b1) * t1 // dg + 1
    return ans        
    

t1, t2 = map(int, input().split())
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
print(solve(t1, t2, a1, a2, b1, b2))