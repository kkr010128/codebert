# B - Tax Rate
N = int(input())
ans = ':('
for x in range(50000):
    if (108*x)//100==N:
        ans = x
        break
print(ans)