S = input()
l = [0] * (len(S)+1)
r = [0] * (len(S)+1)
for i in range(len(S)):
    if S[i] == '<':
        l[i+1] = l[i] + 1
for i in range(len(S)-1,-1,-1):
    if S[i] == '>':
        r[i] = r[i+1] + 1
print(sum([max(l[i],r[i]) for i in range(len(S)+1)]))
