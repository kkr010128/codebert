n, m = input().split()
a = list(map(int, input().split()))
s = 0

for i in a:
    s += int(i)

if int(s) <= int(n):
    print(int(n) - int(s))
else:
    print("-1")