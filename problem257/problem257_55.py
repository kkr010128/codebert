n = int(input())
aas = list(map(int, input().split()))
if n == 1 and aas == [1]:
    print(0)
    exit()
t = 0
for i in aas:
    if i == t + 1:
        t += 1
print(n-t if t > 0 else -1)