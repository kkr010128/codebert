#coding = SJIS

a, b, c, d = map(int, input().split())
ans = "No"

while a * c > 0:
    if ans == "Yes":
        a -= d
        ans = "No"
    else:
        c -= b
        ans = "Yes"

print(ans)