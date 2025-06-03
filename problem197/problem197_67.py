def LI():
    return list(map(int, input().split()))


a, b, c = LI()
if c-a-b < 0:
    ans = "No"
elif 4*a*b < (c-a-b)**2:
    ans = "Yes"
else:
    ans = "No"
print(ans)
