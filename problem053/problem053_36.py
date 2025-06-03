n = input()
l = map(int, raw_input().split())
k = 0
a = []
while n > 0:
    a.append(l[n - 1])
    n -= 1
print ' '.join(map(str, a))