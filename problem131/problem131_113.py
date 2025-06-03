a,v = map(int,input().split())
b,w = map(int,input().split())
t = int(input())
ans = "NO"

if abs(a-b) <= t * (v - w):
    ans = "YES"
    
print(ans)