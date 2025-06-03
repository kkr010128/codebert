n = int(input())

m = n
p = 2
res = 0
st = [0 for i in range(100)]
for i in range(100):
    if i * (i + 1) // 2 >= 100:
        break
    st[i * (i + 1) // 2] = i
for i in range(1, 100):
    st[i] = st[i - 1] if st[i] == 0 else st[i]
#print(st)
while p * p <= n:
    l = 0
    while m % p == 0:
        m //= p
        l += 1
    res += st[l]
    #print(p, res, l)
    p += 1
res += m > 1
print(res)
