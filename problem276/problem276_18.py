n = int(input())
a = list(map(int,input().split()))
iron_len = sum(a)
res = iron_len
st = 0
for i in range(n-1):
    st += a[i]
    res = min(res,abs(iron_len-st*2))
print(res)