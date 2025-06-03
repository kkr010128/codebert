teki, hissatsu = list(map(int, input().split(' ')))
l = sorted(list(map(int, input().split(' '))))[:max(0, teki-hissatsu)]
print(sum(l))