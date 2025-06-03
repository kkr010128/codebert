N = int(input())
S = list(str(input()))

l = [chr(ord('A')+i) for i in range(26)]
p = []
for t in range(len(S)):
    for i in range(26):
        if S[t] == l[i]:
            k = (i+N)%26
            p.append(l[k])
print(''.join(map(str,p)))