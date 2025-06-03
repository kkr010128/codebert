n = int(input())
S = input()
s = []
for i in range(n):
    s.append(S[i])
q = int(input())
BIT = []
for i in range(26):
    B = [0]*(n+1) #1-indexed
    BIT.append(B)

def sum_of_1_to_i(i, LIST):
    z = 0
    while i > 0:
        z += LIST[i]
        i -= i & (-i)
    return z

def update(i, j, LIST):
    while i <= n:
        LIST[i] += j
        i += i & (-i)

for i in range(n):
    k = ord(s[i])-97
    update(i+1, 1, BIT[k])

ans = []

for i in range(q):
    a,b,c = input().split()
    a = int(a)
    b = int(b)
    if a == 1:
        temp = s[b-1]
        if temp == c:
            None
        else:
            update(b, -1, BIT[ord(temp)-97])
            update(b, 1, BIT[ord(c)-97])
            s[b-1] = c
    else:
        c = int(c)
        cur = 0
        for j in range(26):
            if sum_of_1_to_i(c, BIT[j])-sum_of_1_to_i(b-1, BIT[j]) != 0:
                cur += 1
        ans.append(cur)
for i in range(len(ans)):
    print(ans[i])
