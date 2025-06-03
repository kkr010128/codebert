import sys

def judge(word1, word2):
    lena = len(word1)
    lenb = len(word2)
    for i in range(min(lena,lenb)):
        if word1[i] > word2[i]: return 1
        elif word1[i] < word2[i]: return 2
    if lena > lenb: return 1
    elif lena < lenb: return 2
    else: return 0

p = 0
s = [0, 0, 0]
for line in sys.stdin:
    ls = line.strip('\n')
    if p ==0:
        loop = int(ls)
        p = 1
    elif p == 1:
        if loop <= 0: break
        w1, w2 = ls.split()
        tmp = judge(w1, w2)
        if tmp == 0:
            s[1] += 1
            s[2] += 1
        else:
            s[tmp] += 3
        loop -= 1
print s[1], s[2]