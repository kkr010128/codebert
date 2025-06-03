N = int(input())
S = input()
'''
Editorialのヒントを参照しました。
000 ~ 999の実現可能性を考えます。
'''
L = []
s = ''
Comb = 0
key_k = False
for i in range(0, 10):
    for j in range(0, 10):
        if key_k is not True:
            s += str(j)
        else:
            s += str(i)
            s += str(j)
            key_k = False
        for k in range(0, 10):
            s += str(k)
            L.append(s)
            s = ''
            s += str(i)
            s += str(j)
        s = ''
        key_k = True
L.remove(L[0])
L.append('000') #生成、もう少し短くしたい
S_copy = S
A = []
for el in L:
    c0 = el[0]
    c1 = el[1]
    c2 = el[2]
    S = S_copy
    N0 = S.find(c0)
    if N0 == -1:
        continue
    else:
        S = S[N0+1::]
        N1 = S.find(c1)
        if N1 == -1:
            continue
        else:
            S = S[N1+1::]
            N2 = S.find(c2)
            if N2 == -1:
                continue
            else:
                Comb += 1
print(Comb)