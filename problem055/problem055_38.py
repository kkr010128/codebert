a = [[[0 for r in range (10)] for f in range(3)] for b in range(4)]
ans = ""

n = input()
for i in range(0, n):
    b, f, r, v = map(int, raw_input().split(" "))
    a[b-1][f-1][r-1] += v

for b in range(4):
    for f in range(3):
        for r in range(10):
            ans += " "+str(a[b][f][r])
        if (b!=3 or f!=2 or r!=9):
            ans += "\n"
    if (b != 3):
        ans += "#"*20+"\n"

print(ans)