from collections import Counter
n = int(input())
a = list(map(int,input().split()))
a.sort()
ct = Counter(a)
st = set()
ans = 0
x = max(a)
for i in range(n):
    if a[i] in st:
        continue
    if ct[a[i]]>1:
        st.add(a[i])
    for j in range(2,x//a[i]+1):
        st.add(a[i]*j)
for i in range(n):
    if not a[i] in st:
        ans += 1
print(ans)