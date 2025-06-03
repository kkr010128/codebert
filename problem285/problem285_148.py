from itertools import groupby

s = input()
A = [(key, sum(1 for _ in group)) for key, group in groupby(s)]
tmp = 0
ans = 0
for key, count in A:
    if key == '<':
        ans += count*(count+1)//2
        tmp = count
    else:
        if tmp < count:
            ans -= tmp
            ans += count
        ans += (count-1)*count//2
        tmp = 0
print(ans)
