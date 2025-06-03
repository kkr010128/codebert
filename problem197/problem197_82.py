a, b, c = map(int, input().split())
sahen = 4*a*b
uhen = (c-a-b)**2
if c-a-b < 0:
    ans = "No"
elif sahen < uhen:
    ans = "Yes"
else:
    ans = "No"
print(ans)
