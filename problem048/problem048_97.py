n = input()
a = map(int,raw_input().split())
s = 0
m = a[0]
M = a[0]
for i in range(0,n):
    s = s + a[i]
    if m > a[i]:
        m = a[i]
    if M < a[i]:
        M = a[i]
print m,M,s