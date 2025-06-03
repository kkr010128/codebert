import sys
input = sys.stdin.readline

S=tuple(input().strip())
N=len(S)+1
sets = []
count = 0

for c in S:
    d = 1 if c == '<' else -1
    if count * d < 0:
        sets.append(count)
        count = d
    else:
        count += d
sets.append(count)

sum = 0
for i in range(len(sets)):
    k=sets[i]
    if k > 0:
        sum += (k*(k+1))//2
    else:
        sum += (k*(k-1))//2
        if i > 0:
            sum -= min(sets[i-1], -k)

print(sum)
