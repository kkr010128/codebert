nkc = list(map(int, input().split()))
s = input()
ok = [i for i in range(nkc[0]) if s[i]=='o']

L = []
today = -1000000
for x in ok:
    if x-today >= nkc[2]+1:
        today = x
        L.append(x)
    if len(L) == nkc[1]:
        break

R = []
today = 1000000
ok.reverse()
for x in ok:
    if today-x >= nkc[2]+1:
        today = x
        R.append(x)
    if len(R) == nkc[1]:
        break

R.reverse()
for i in range(nkc[1]):
    if L[i] == R[i]:
        print(L[i]+1)