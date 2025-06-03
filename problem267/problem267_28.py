n = int(input())
s = input()
ans = 0
for i in range(1000):
    i = str(i).zfill(3)
    f = True
    x = -1
    for j in range(3):
        x = s.find(i[j],x+1)
        f = f and bool(x >= 0)
    ans += f
print(ans)
