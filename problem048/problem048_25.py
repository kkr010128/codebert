n = input()
l = map(int, raw_input().split())
max = l[0]
min = l[0]
s = l[0]
k = 1
while k < n:
    if max < l[k]:
        max = l[k]
    if min > l[k]:
        min = l[k]
    s = s + l[k]
    k = k + 1
print min, max, s