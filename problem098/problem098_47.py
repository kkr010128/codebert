N = int(input())
c = input()
red = 0

for i in c:
    if i=="R":
        red += 1

br = 0
ans = 10**12 if red else 0
for i in range(red):
    if c[i]=="R":
        br += 1
    white = i+1 - br
    disappear = red - br - white
    ans = min(ans, white+disappear)

print(ans)
