s = list(input())
al = [0]*(len(s)+1)

for i in range(len(s)):
    if s[i] == '<':
        al[i+1] = max(al[i]+1, al[i+1])

for i in range(len(s)-1, -1, -1):
    if s[i] == '>':
        al[i] = max(al[i+1]+1, al[i])

print(sum(al))