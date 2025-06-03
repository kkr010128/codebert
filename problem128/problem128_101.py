X, N = map(int, input().split())

try:
    p = list(map(int, input().split()))
except:
    p = []
i = 0

while True:
    if X + i not in p:
        ans = X + i
        if X - i not in p:
            ans = X - i
        break
    if X - i not in p:
        ans = X - i
        break
    
    i += 1

print(ans)