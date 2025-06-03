a, b = map(float, input().split())

a = round(a)
b = round(b*100)
ans = a*b
ans = str(ans)[:-2]

if ans == "":
    ans = 0

print(ans)