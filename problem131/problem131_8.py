a,v = map(int, input().split())
b,w = map(int, input().split())
t = int(input())

ans = "NO"
if a > b: a,b = a*(-1), b*(-1)
if a == b: ans = "YES"
elif a < b:
    if v > w and (b-a) <= (v-w)*t: ans = "YES"
print(ans)